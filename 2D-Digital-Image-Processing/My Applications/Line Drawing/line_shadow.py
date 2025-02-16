import cv2
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# 加载原始图片
image = cv2.imread('images/001.jpg')

# 转换为灰度图
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 使用高斯模糊减少噪点
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# 使用Canny边缘检测提取色块的外轮廓
edges = cv2.Canny(blurred, 100, 200)

# 创建透明背景
height, width = edges.shape

# 转换为HSV颜色空间
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 提取阴影区域：低亮度区域（低V值）
lower_shadows = np.array([0, 0, 0])  # 阴影的低阈值
upper_shadows = np.array([180, 255, 80])  # 阴影的高阈值

# 阈值处理，提取阴影区域
shadow_mask = cv2.inRange(hsv, lower_shadows, upper_shadows)

# 使用Canny边缘检测提取阴影外轮廓
shadow_edges = cv2.Canny(shadow_mask, 100, 200)

# 创建透明背景图
transparent_bg_shadows = np.zeros((height, width, 4), dtype=np.uint8)

# 将Canny检测到的边缘填充为黑色线条
transparent_bg_shadows[:, :, 3] = shadow_edges  # 设置透明通道为阴影边缘图像

# 使用形态学操作闭合阴影区域
kernel = np.ones((5, 5), np.uint8)
shadow_edges_closed = cv2.dilate(shadow_edges, kernel, iterations=2)

# 更新图像以确保闭合
transparent_bg_shadows[:, :, 3] = shadow_edges_closed

# 保存结果
cv2.imwrite('output/line_shadow.png', transparent_bg_shadows)

# 显示结果
plt.imshow(transparent_bg_shadows)
plt.title("Shadow Outlines")
plt.axis('off')
plt.show()
