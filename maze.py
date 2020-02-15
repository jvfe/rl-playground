import numpy as np

class Agent:
    def __init__(self, i=0, j=0):
        self.i = i
        self.j = j

    @property
    def loc(self):
        return(self.i, self.j)

    def vmove(self, direction):
        direction = 1 if direction > 0 else -1
        Agent(self.i + direction, self.j)

    def hmove(self, direction):
        direction = 1 if direction > 0 else -1
        Agent(self.i, self.j + direction)
        
    def __repr__(self):
        return str(self.loc)

class Maze:
    def __init__(self, rows=4, columns=4):
        self.env = np.zeros((4,4))
        self.mouse = Agent(0, 0)

    def in_bounds(self, i, j):
        nr, nc = self.env.shape
        return i >= 0 and i < nr and j >= 0 and j < nc

    def agent_in_bounds(self, a):
        return self.in_bounds(a.i, a.j)
    
    def agent_would_die(self, a):
        return not self.env[a.i, a.j]==-1

    def compute_moves(self):
        a = self.mouse
        moves = [
                a.vmove(1),
                a.vmove(-1),
                a.hmove(1),
                a.hmove(-1),
        ]
        return [m for m in moves if self.agent_in_bounds(m) and not self.agent_would_die(m)]

    def visualize(self):
        assert self.agent_in_bounds(self.mouse), "Mouse is out of bounds"
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
    e[3, 0:2] = -1
    return m

if __name__ == '__main__':
    m = make_test_maze() 
    m.mouse = m.mouse.vmove(1)
    m.visualize()

    print(m.compute_moves())

