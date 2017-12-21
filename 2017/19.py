import os

def load(path):
    assert os.path.exists(path)

    return [
        [c for c in line.rstrip()]
        for line in open(path).readlines()
    ]

def walk(diagram):

    # Find first position
    x = diagram[0].index('|')
    y = 0
    dx, dy = (0, 1)

    def _char(x, y):
        try:
            char = diagram[y][x]
            if char == ' ':
                return
            return char
        except:
            return

    out = ''
    nb = 0
    while True:
        # Analyse current char
        char = _char(x, y)
        if char is None:
            break # endgame
        if char.isalpha():
            out += char

        if char == '+':
            # Direction change
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (-1 * i, -1 * j) == (dx, dy) or (i, j) == (dx, dy):
                    # skip previous direction
                    continue

                char = _char(x+i, y+j)
                if char is not None:
                    # found new direction
                    dx, dy = i, j
                    break

        # New positions
        x, y = x+dx, y+dy
        nb += 1

    return out, nb

if __name__ == '__main__':
    sample = load('19.sample.txt')
    real = load('19.txt')

    assert walk(sample) == ('ABCDEF', 38)
    print(walk(real))

