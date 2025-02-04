import numpy as np

import gudhi

# 创建一个简单的简单形状
points = np.random.rand(10, 2)  # 随机生成10个二维点
simplex_tree = gudhi.SimplexTree()

# 创建一个简单的单纯复形
for i in range(10):
    simplex_tree.insert([i])  # 插入点
for i in range(9):
    simplex_tree.insert([i, i + 1])  # 插入边

# 计算同调群
simplex_tree.compute_persistence()
