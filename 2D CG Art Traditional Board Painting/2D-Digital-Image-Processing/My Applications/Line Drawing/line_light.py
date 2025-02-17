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

# 提取高光区域：亮度较高的部分（V通道高）
lower_highlights = np.array([0, 0, 200])  # 高光的低阈值
upper_highlights = np.array([180, 255, 255])  # 高光的高阈值

# 阈值处理，分离高光区域
highlight_mask = cv2.inRange(hsv, lower_highlights, upper_highlights)

# 使用Canny边缘检测提取高光外轮廓
highlight_edges = cv2.Canny(highlight_mask, 50, 150)

# 创建透明背景
transparent_bg_highlights = np.zeros((height, width, 4), dtype=np.uint8)  # 4通道：BGR + Alpha

# 将Canny检测到的边缘填充为黑色线条
transparent_bg_highlights[:, :, 3] = highlight_edges  # 设置透明通道为高光边缘图像

# 保存结果
cv2.imwrite('output/line_light.png', transparent_bg_highlights)

# 显示结果
plt.imshow(transparent_bg_highlights)
plt.title("Highlight Outlines")
plt.axis('off')
plt.show()
