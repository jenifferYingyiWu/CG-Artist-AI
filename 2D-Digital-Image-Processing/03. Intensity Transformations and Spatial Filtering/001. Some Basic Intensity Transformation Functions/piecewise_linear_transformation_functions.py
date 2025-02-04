import cv2
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)


# 定义分段线性变换函数
def piecewise_linear(image):
    # 设定阈值进行分段
    threshold1 = 85
    threshold2 = 170
    # 创建一个空白图像
    result = np.zeros_like(image)

    # 小于 threshold1 的像素
    result[image < threshold1] = (image[image < threshold1] * 1.5).clip(0, 255)
    # 在 threshold1 和 threshold2 之间的像素
    result[(image >= threshold1) & (image < threshold2)] = (
            image[(image >= threshold1) & (image < threshold2)] * 1.2).clip(0, 255)
    # 大于 threshold2 的像素
    result[image >= threshold2] = (image[image >= threshold2] * 0.8).clip(0, 255)

    return result


# 进行分段线性变换
image_piecewise = piecewise_linear(image)

# 显示分段线性变换后的图像
plt.subplot(1, 2, 1), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(1, 2, 2), plt.imshow(image_piecewise, cmap='gray'), plt.title('Piecewise Linear Transformed Image')
plt.show()
