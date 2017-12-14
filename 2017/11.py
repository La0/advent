directions = {
    'n': (0, 1, -1),
    's': (0, -1, 1),
    'nw': (-1, 1, 0),
    'sw': (-1, 0, 1),
    'ne': (1, 0, -1),
    'se': (1, -1, 0),
}

def steps(path):
    steps = path.split(',')

    # Cube distance
    # https://www.redblobgames.com/grids/hexagons/
    x, y, z = map(sum, zip(*[directions[s] for s in steps]))
    return (abs(x) + abs(y) + abs(z)) / 2

def furthest(path):
    all_steps = path.split(',')
    distances = [
        steps(','.join(all_steps[:i]))
        for i in range(1, len(all_steps))
    ]
    return max(distances)

if __name__ == '__main__':
    assert steps('se,sw,se,sw,sw') == 3
    assert steps('ne,ne,s,s') == 2
    assert steps('ne,ne,sw,sw') == 0
    assert steps('ne,ne,ne') == 3
    with open('11.txt') as f:
        path = f.read().rstrip()
        print(steps(path))
        print(furthest(path))
