

def is_wall(x, y, favorite_number):
    if x < 0 or y < 0:
        return None
    out = x*x + 3*x + 2*x*y + y + y*y
    out += favorite_number
    binary = '{0:b}'.format(out)
    return len([b for b in binary if b == '1']) % 2 == 1

def distance(ax, ay, bx, by):
    return abs(bx - ax) + abs(by - ay)

def solve(final_x, final_y, favorite_number):

    done = []
    queue = [(0,0,distance(0, 0, final_x, final_y), 0)] # start
    solutions = []
    while len(queue) > 0:
        x,y,d,s = queue.pop(0)

        if d == 0:
            solutions.append(s)
            print(solutions)
        done.append((x,y))

        # Add neighbors to queue
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i,j) == (0,0):
                    continue # current pos
                nx, ny = x+i, y+j
                if (nx,ny) in done:
                    continue # already passed
                done.append((nx, ny))
                wall = is_wall(nx, ny, favorite_number)
                if wall is None or wall is True:
                    continue # invalid position
                d = distance(nx, ny, final_x, final_y)
                queue.append((nx, ny, d, s + abs(i) + abs(j)))
                #print(nx, ny, wall)

    print(solutions)
    return min(solutions)


if __name__ == '__main__':
    assert not is_wall(0,0, 10)
    assert ''.join([is_wall(i, 0, 10) and '#' or '.' for i in range(10)]) == '.#.####.##'
    x = solve(7,4, 10)
    print(x)
