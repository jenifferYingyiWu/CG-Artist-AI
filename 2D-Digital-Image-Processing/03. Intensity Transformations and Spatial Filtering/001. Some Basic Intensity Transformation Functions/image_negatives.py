import cv2
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)  # 转为灰度图

# 图像反转
image_negative = 255 - image

# 显示原始图像与反转后的图像
plt.subplot(1, 2, 1), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(1, 2, 2), plt.imshow(image_negative, cmap='gray'), plt.title('Image Negative')
plt.show()
