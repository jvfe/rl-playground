import numpy as np

class Agent:
    def __init__(self, i=0, j=0):
        self.i = i
        self.j = j

class Maze:
    def __init__(self, rows=4, columns=4):
        self.env = np.zeros((4,4))
        self.mouse = Agent(0, 0)

    def in_bounds(self, i, j):
        nr, nc = self.env.shape
        return i > 0 and i < nr and j > 0 and j < nc

    def visualize(self):
        e = self.env.copy()
        m = self.mouse
        e[m.i, m.j] = 6
        print(e)

def make_test_maze():
    m = Maze()
    e = m.env
    e[3,3] = 1
    e[0,1:3] = -1
    e[1, 2:] = -1
    e[2, 0] = -1
    e[3, 0:2] = -1
    return m

if __name__ == '__main__':
    m = make_test_maze() 
    m.mouse.i = 1
    m.visualize()
