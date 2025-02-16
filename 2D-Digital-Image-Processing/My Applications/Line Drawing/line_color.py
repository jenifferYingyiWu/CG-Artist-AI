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
transparent_bg = np.zeros((height, width, 4), dtype=np.uint8)  # 4通道：BGR + Alpha
transparent_bg[:, :, 3] = edges  # 将边缘图作为透明通道

# 保存结果
cv2.imwrite('output/line_color.png', transparent_bg)

# 显示结果
plt.imshow(transparent_bg)
plt.title("Color Block Outlines")
plt.axis('off')
plt.show()
