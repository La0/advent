import math

def steps(n):
    if n == 1:
        return 0

    above = int(math.ceil(math.sqrt(n)))
    if above % 2 == 0:
        above += 1
    end = above ** 2
    start = (above - 2) ** 2
    assert end >= n >= start

    distance = (above - 1) / 2
    side = above - 1
    x = (n - start) % side
    axis_dist = (x - side / 2)

    return axis_dist + distance

if __name__ == '__main__':
    assert steps(23) == 2
    assert steps(12) == 3
    assert steps(1024) == 31
    assert steps(1) == 0
    print(steps(277678))
