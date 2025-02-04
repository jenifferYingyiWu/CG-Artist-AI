import cv2
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# 对数变换
c = 255 / np.log(1 + np.max(image))  # 常数 c 用来调整对比度
log_image = c * np.log(1 + image)

# 显示对数变换后的图像
plt.subplot(1, 2, 1), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(1, 2, 2), plt.imshow(log_image, cmap='gray'), plt.title('Log Transformed Image')
plt.show()
