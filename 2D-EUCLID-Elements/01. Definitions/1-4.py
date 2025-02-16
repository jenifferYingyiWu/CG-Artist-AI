import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# 1. A point is that which has no part
# 点的定义，我们只画一个点
point = [2, 3]

# 2. A line is breadthless length
# 线的定义，画出一条从点(0, 0)到(4, 4)的直线
x_line = [0, 4]
y_line = [0, 4]

# 3. The extremities of a line are points
# 画出直线的端点
line_start = [0, 0]
line_end = [4, 4]

# 4. A straight line is a line which lies evenly with the points on itself
# 画出直线连接的一系列点
x_straight_line = [i for i in range(5)]
y_straight_line = [i for i in range(5)]

# 创建图形
fig, ax = plt.subplots()

# 绘制点
ax.scatter(*point, color='red', label="Point (2, 3)")

# 绘制直线
ax.plot(x_line, y_line, label="Line from (0,0) to (4,4)", color='blue')

# 绘制线的端点
ax.scatter(*line_start, color='green', zorder=5, label="Start Point (0, 0)")
ax.scatter(*line_end, color='green', zorder=5, label="End Point (4, 4)")

# 绘制直线的点集合
ax.plot(x_straight_line, y_straight_line, label="Straight Line", color='orange')

# 设置图形显示
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 5)
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_title("Euclidean Geometry Visualized in Python")
ax.legend()

plt.grid(True)
plt.show()
