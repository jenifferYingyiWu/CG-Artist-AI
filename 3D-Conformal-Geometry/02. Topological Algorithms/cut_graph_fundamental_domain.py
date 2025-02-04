import trimesh

import numpy as np
import scipy.spatial

# 创建一个简单的3D网格
mesh = trimesh.load_mesh('哑铃.obj')

# 假设已有一个3D网格（用三角形表示）
vertices = np.array(mesh.vertices)
faces = mesh.faces

# 基于面片的连接性，寻找切割线
# 可以使用基于图的最短路径算法
