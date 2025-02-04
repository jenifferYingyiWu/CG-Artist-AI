import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from sklearn.decomposition import DictionaryLearning

# 创建示例数据
X = np.random.randn(100, 20)  # 100个样本，20个特征

# 稀疏编码
dict_learn = DictionaryLearning(n_components=10, transform_n_nonzero_coefs=5)
X_sparse = dict_learn.fit_transform(X)

# 绘图
plt.imshow(X_sparse, cmap='gray')
plt.title('Sparse Coding')
plt.colorbar()
plt.show()
