import numpy as np

from src.rrt.rrt import RRT
from src.search_space.search_space import SearchSpace
from src.utilities.plotting import Plot

# x right
# y down
# z forward
dimensions = np.array([(-5, 5), (-5, 5), (-1, 9)])
obstacles = np.array([(-5, -0.5, 4, 5, 0.5, 5)])
start = (0, 0, 0)
goal = (0, 0, 9)
q = [(0.5, 3)]
r = 0.1
max_samples = 128
prc = 0.1

space = SearchSpace(dimensions, obstacles)
rrt = RRT(space, q, start, goal, max_samples, r, prc)
path = rrt.rrt_search()

plot = Plot("eoc_rrt")
plot.plot_tree(space, rrt.trees)
if path is not None:
    plot.plot_path(space, path)
plot.plot_obstacles(space, obstacles)
plot.plot_start(space, start)
plot.plot_goal(space, goal)
plot.draw(auto_open=True)
