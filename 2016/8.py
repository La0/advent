import re

COLS = 50
ROWS = 6

regex_rect = re.compile('rect (\d+)x(\d+)')
regex_col = re.compile('rotate column x=(\d+) by (\d+)')
regex_row = re.compile('rotate row y=(\d+) by (\d+)')

def rect(screen, x, y):
    for i in range(y):
        for j in range(x):
            screen[i][j] = '#'
    return screen

def col(screen, x, offset):
    new_col = [screen[(i-offset)%ROWS][x] for i in range(ROWS)]
    for i in range(ROWS):
        screen[i][x] = new_col[i]

    return screen

def row(screen, y, offset):
    screen[y] = [screen[y][(i-offset)%COLS] for i in range(COLS)]
    return screen

def build_screen(lines):
    # clean screen
    screen = [x[:] for x in [['.'] * COLS] * ROWS]

    for line in lines:

        out = regex_rect.match(line)
        if out:
            x,y = map(int, out.groups())
            screen = rect(screen, x, y)

        out = regex_col.match(line)
        if out:
            x,o = map(int, out.groups())
            screen = col(screen, x, o)

        out = regex_row.match(line)
        if out:
            y,o = map(int, out.groups())
            screen = row(screen, y, o)

        #display(screen)

    return screen

def display(screen):
    print('\n'.join([''.join(l) for l in screen]))

if __name__ == '__main__':
    with open('8.txt') as f:
        s = build_screen(f.readlines())
        display(s)
        nb = len([s[y][x] for x in range(COLS) for y in range(ROWS) if s[y][x] != '.'])
        print(nb)
