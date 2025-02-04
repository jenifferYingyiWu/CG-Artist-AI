import trimesh

# 创建一个简单的3D网格
mesh = trimesh.load_mesh('哑铃.obj')

# 查看网格的拓扑
print(mesh.faces)
print(mesh.vertices)
