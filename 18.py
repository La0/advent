class Grid(object):
    """
    Game of Life !
    """

    def __init__(self, filename):
        self.grid = []

        with open(filename, 'r') as f:
            for line in f.readlines():
                line = line.replace('\n', '')
                self.grid.append([c for c in line])

        self.ymax = len(self.grid)
        self.xmax = len(self.grid[0])

        print 'Initial'
        self.debug()

    def run(self, limit):
        for i in range(1, limit+1):
            cpt = 0
            self.new_grid = [['.' for x in range(self.xmax)] for y in range(self.ymax)]

            # Evolve full grid one step forward
            for y in range(0, len(self.grid)):
                for x in range(0, len(self.grid[y])):
                    alive = self.eval(x, y)
                    if alive:
                        cpt += 1
                        char = '#'
                    else:
                        char = '.'

                    # Save new result
                    self.new_grid[y][x] = char

            self.grid = self.new_grid
            print 'Step', i, cpt
            #self.debug()

    def debug(self):
        # Display current grid
        print '-' * 80
        for l in self.grid:
            print ''.join(l)


    def eval(self, x, y):

        # Calc valid positions
        offsets = [(a,b) for a in range(-1, 2) for b in range(-1, 2)]
        offsets.remove((0, 0))
        positions = map(lambda o : (o[0]+x, o[1]+y), offsets)
        positions = filter(lambda p : 0 <= p[0] < self.xmax, positions)
        positions = filter(lambda p : 0 <= p[1] < self.ymax, positions)

        # Apply rules
        alive = self.grid[y][x] == '#'
        nb = len(filter(lambda p : self.grid[p[1]][p[0]] == '#', positions))

        # A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
        if alive and nb in (2, 3):
            return True

        # A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
        if not alive and nb == 3:
            return True

        return False

if __name__ == '__main__':
    grid = Grid('18.input')
    grid.run(100)
