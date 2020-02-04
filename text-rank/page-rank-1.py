# from https://towardsdatascience.com/textrank-for-keyword-extraction-by-python-c0bae21bcec0
import numpy as np

g = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [1, 0.5, 0, 0],
     [0, 0.5, 0, 0]]

g = np.array(g)
pr = np.array([1, 1, 1, 1])   # initial weights of all pages a, b, e, f
d = 0.85

for iter in range(10):
    pr = 0.15 + 0.85 * np.dot(g, pr)
    print(iter)
    print(pr)
