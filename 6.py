import re

class Grid(object):

    def __init__(self, x, y):
        self.cells = []
        for i in range(0, y):
            self.cells.append([])
            for j in range(0, x):
                self.cells[i].append(False)

    def read(self, line):
        """
        React to instructions
        """
        print line
        res = re.search(r'([\w\s]+) (\d+),(\d+) through (\d+),(\d+)', line)
        action, xa, ya, xb, yb = res.groups()

        for i in range(int(ya), int(yb) + 1):
            for j in range(int(xa), int(xb) + 1):
                self.update(action, j, i)

    def update(self, action, x, y):
        if action == 'turn off':
            self.cells[y][x] = False

        elif action == 'turn on':
            self.cells[y][x] = True

        elif action == 'toggle':
            self.cells[y][x] = not self.cells[y][x]

    def count(self):
        return sum([sum(x) for x in self.cells])

if __name__ == '__main__':
    g = Grid(1000, 1000)
    with open('6.input', 'r') as f:
        for line in f.readlines():
            g.read(line.replace('\n',''))

    print g.count()
