import cv2
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# 加载图像
image = cv2.imread('images/001.jpg')

# 转换为灰度图
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 高斯模糊，减少噪声
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# 使用Canny边缘检测提取色块外轮廓
edges = cv2.Canny(blurred, 50, 150)

# 创建透明背景
height, width = edges.shape

# 转换为HSV颜色空间
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 提取阴影区域：假设阴影的亮度较低
lower_shadows = np.array([0, 0, 0])  # 阴影的低阈值
upper_shadows = np.array([180, 255, 80])  # 阴影的高阈值

# 阈值处理，提取阴影区域
shadow_mask = cv2.inRange(hsv, lower_shadows, upper_shadows)

# 使用Canny边缘检测提取阴影外轮廓
shadow_edges = cv2.Canny(shadow_mask, 50, 150)

# 创建透明背景
transparent_bg_shadows = np.zeros((height, width, 4), dtype=np.uint8)  # 4通道：BGR + Alpha

# 将Canny检测到的边缘填充为黑色线条
transparent_bg_shadows[:, :, 3] = shadow_edges  # 设置透明通道为阴影边缘图像

# 保存结果
cv2.imwrite('output/line_shadow.png', transparent_bg_shadows)

# 显示结果
plt.imshow(transparent_bg_shadows)
plt.title("Shadow Outlines")
plt.axis('off')
plt.show()
