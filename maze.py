import numpy as np

class Maze:
    def __init__(self, rows=4, columns=4):
        self.env = np.zeros((4,4))

if __name__ == '__main__':
    m = Maze()
    print(m.env)
