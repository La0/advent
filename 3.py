import operator

def list_gifts(line):
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

    return len(grid)

if __name__ == '__main__':
    with open('3.input', 'r') as f:
        print list_gifts(f.read())
