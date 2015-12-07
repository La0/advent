import operator

def list_gifts(line, raw=False):
    grid = {}
    position = (0, 0) # Starting pos
    moves = {
        '^' : (0, 1),
        '>' : (1, 0),
        'v' : (0, -1),
        '<' : (-1, 0),
    }

    def _gift(pos):
        if pos not in grid:
            grid[pos] = 0
        grid[pos] += 1

    _gift(position)
    for move in line:
        position = tuple(map(operator.add, position, moves.get(move, (0, 0))))
        #print position
        _gift(position)

    return raw and grid or len(grid)


def list_gifts_robo(line):
    """
    Same as above but with two players
    """
    grid = {}
    santa_line = ''.join([line[i] for i in range(0, len(line), 2)])
    grid.update(list_gifts(santa_line, raw=True))
    robo_line = ''.join([line[i] for i in range(1, len(line), 2)])
    grid.update(list_gifts(robo_line, raw=True))

    return len(grid)

if __name__ == '__main__':
    with open('3.input', 'r') as f:
        print list_gifts_robo(f.read())
