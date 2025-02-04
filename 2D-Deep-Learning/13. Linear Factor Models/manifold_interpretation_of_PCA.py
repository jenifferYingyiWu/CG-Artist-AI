import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

# 创建示例数据
X = np.random.randn(100, 50)  # 100个样本，50个特征

# 使用PCA降维
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# 使用t-SNE可视化
tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(X_pca)

# 绘图
plt.scatter(X_tsne[:, 0], X_tsne[:, 1])
plt.title('Manifold Interpretation of PCA using t-SNE')
plt.show()
