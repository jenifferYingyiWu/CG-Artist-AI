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

# 提取高光区域：亮度较高的部分（V通道高）
lower_highlights = np.array([0, 0, 200])  # 高光的低阈值
upper_highlights = np.array([180, 255, 255])  # 高光的高阈值

# 阈值处理，提取高光区域
highlight_mask = cv2.inRange(hsv, lower_highlights, upper_highlights)

# 使用Canny边缘检测提取高光外轮廓
highlight_edges = cv2.Canny(highlight_mask, 100, 200)

# 创建透明背景图
transparent_bg_highlights = np.zeros((height, width, 4), dtype=np.uint8)

# 将Canny检测到的边缘填充为黑色线条
transparent_bg_highlights[:, :, 3] = highlight_edges  # 设置透明通道为高光边缘图像

# 使用形态学操作闭合高光区域
kernel = np.ones((5, 5), np.uint8)
highlight_edges_closed = cv2.dilate(highlight_edges, kernel, iterations=2)

# 更新图像以确保闭合
transparent_bg_highlights[:, :, 3] = highlight_edges_closed

# 保存结果
cv2.imwrite('output/line_light.png', transparent_bg_highlights)

# 显示结果
plt.imshow(transparent_bg_highlights)
plt.title("Highlight Outlines")
plt.axis('off')
plt.show()
