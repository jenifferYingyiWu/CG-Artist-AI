import cv2
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# 伽马变换
gamma = 2.2  # 伽马值
gamma_corrected = np.array(255 * (image / 255) ** gamma, dtype='uint8')

# 显示伽马变换后的图像
plt.subplot(1, 2, 1), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(1, 2, 2), plt.imshow(gamma_corrected, cmap='gray'), plt.title('Gamma Transformed Image')
plt.show()
