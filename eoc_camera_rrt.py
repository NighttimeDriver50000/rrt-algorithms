import json
import sys
import numpy as np

from src.rrt.rrt import RRT
from src.search_space.search_space import SearchSpace
from src.utilities.plotting import Plot

dimensions = np.array([(0, 221), (0, 124), (0, 20)])
obstacles = np.array(json.load(open(sys.argv[1])))
start = (110, 71, 0)
goal = (110, 71, 10)
q = [(3, 3)]
r = 1
max_samples = 128
prc = 0.1

space = SearchSpace(dimensions, obstacles)
rrt = RRT(space, q, start, goal, max_samples, r, prc)
path = rrt.rrt_search()

plot = Plot("eoc_camera_rrt")
plot.plot_tree(space, rrt.trees)
if path is not None:
    plot.plot_path(space, path)
plot.plot_obstacles(space, obstacles)
plot.plot_start(space, start)
plot.plot_goal(space, goal)
plot.draw(auto_open=True)
