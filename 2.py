def solve(lines):
    pad = (
        (0, 0, 1, 0, 0),
        (0, 2, 3, 4, 0),
        (5, 6, 7, 8, 9),
        (0, 'A', 'B', 'C', 0),
        (0, 0, 'D', 0, 0),
    )
    directions = {
      'U' : (0, -1),
      'D' : (0, 1),
      'L' : (-1, 0),
      'R' : (1, 0),
    }
    out = []
    x, y = 0, 2 # start from 5
    for line in lines:
        for vx, vy in [directions[c] for c in line.replace('\n', '')]:
            xx = max(0, min(4, x + vx))
            yy = max(0, min(4, y + vy))
            try:
                c = pad[yy][xx]
                if c == 0:
                    raise Exception('Invalid char')
            except:
                continue

            x, y = xx, yy

        out.append(pad[y][x])
    return ''.join(map(str, out))


if __name__ == '__main__':
    with open('2.txt') as f:
        print(solve(f.readlines()))
