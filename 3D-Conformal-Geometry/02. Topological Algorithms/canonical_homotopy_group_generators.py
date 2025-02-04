import gudhi

simplex_tree = gudhi.SimplexTree()

# 获取同伦群的生成元
simplex_tree.compute_persistence()
persistence_intervals = simplex_tree.persistence_intervals_in_dimension(1)

# 可以通过生成元来表示同伦群
