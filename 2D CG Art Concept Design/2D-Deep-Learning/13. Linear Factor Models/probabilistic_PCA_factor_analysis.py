import numpy as np
from sklearn.decomposition import PCA, FactorAnalysis
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# 创建示例数据
X = np.random.randn(100, 5)  # 100个样本，5个特征

# PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Factor Analysis
fa = FactorAnalysis(n_components=2)
X_fa = fa.fit_transform(X)

# 绘图比较
plt.subplot(1, 2, 1)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c='blue', label='PCA')
plt.title('PCA')

plt.subplot(1, 2, 2)
plt.scatter(X_fa[:, 0], X_fa[:, 1], c='red', label='Factor Analysis')
plt.title('Factor Analysis')

plt.show()
