def solve(lines):
    pad = (
      (1, 2, 3),
      (4, 5, 6),
      (7, 8, 9),
    )
    directions = {
      'U' : (0, -1),
      'D' : (0, 1),
      'L' : (-1, 0),
      'R' : (1, 0),
    }
    out = []
    x, y = 1, 1 # start from 5
    for line in lines:
        for vx, vy in [directions[c] for c in line.replace('\n', '')]:
            x = max(0, min(2, (x + vx)))
            y = max(0, min(2, (y + vy)))

        out.append(pad[y][x])
    return ''.join(map(str, out))


if __name__ == '__main__':
    with open('2.txt') as f:
        print(solve(f.readlines()))
