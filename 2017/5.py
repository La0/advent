def search_exit(steps):
    assert isinstance(steps, list)
    n = 0
    index = 0
    while 0 <= index < len(steps):
        value = steps[index]
        steps[index] += 1
        index += value
        n += 1
    return n


def search_exit2(steps):
    assert isinstance(steps, list)
    n = 0
    index = 0
    while 0 <= index < len(steps):
        value = steps[index]
        steps[index] += value >= 3 and -1 or 1
        index += value
        n += 1
    return n


if __name__ == '__main__':
    assert search_exit([0, 3, 0, 1, -3]) == 5

    with open('5.txt') as f:
        steps = list(map(int, f.readlines()))
        print(search_exit(steps))

    assert search_exit2([0, 3, 0, 1, -3]) == 10

    with open('5.txt') as f:
        steps = list(map(int, f.readlines()))
        print(search_exit2(steps))
