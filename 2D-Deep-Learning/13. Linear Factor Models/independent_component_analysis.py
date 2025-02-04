import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from sklearn.decomposition import FastICA

# 创建示例数据（两个信号源的混合）
S = np.c_[np.sin(2 * np.pi * 0.03 * np.arange(1000)),
np.sign(np.sin(2 * np.pi * 0.05 * np.arange(1000)))]
S += 0.2 * np.random.randn(1000, 2)  # 添加噪声
S /= S.std(axis=0)

# 通过ICA分离信号
ica = FastICA(n_components=2)
S_ = ica.fit_transform(S)  # 估计源信号
A_ = ica.mixing_  # 混合矩阵

# 绘图
plt.figure(figsize=(7, 7))
plt.subplot(2, 1, 1)
plt.title('Mixed Signals')
plt.plot(S)

plt.subplot(2, 1, 2)
plt.title('Recovered Signals')
plt.plot(S_)

plt.show()
