import hashlib
from collections import namedtuple

Hash = namedtuple('Hash', 'index, hash, char')


def is_triplet(x):
    for c in '0123456789abcdef':
        if c*3 in x:
            return c

def is_five(x, c):
    return c*5 in x

def stretch(x):
    for i in range(2017):
        x = hashlib.md5(x).hexdigest()
    return x


def solve(salt):
    valid = []
    running = []

    i = 0
    while len(valid) <= 64:
        contents = '{}{}'.format(salt, i)
        h = stretch(contents)
        current = Hash(i, h, is_triplet(h))

        for run in running:
            # still running ?
            if current.index - run.index > 1000 or run in valid:
                continue

            # has match ?
            if is_five(current.hash, run.char):
                valid.append(run)
                print(run)

        # Triplet ?
        if current.char is not None:
            running.append(current)

        i += 1

    return sorted(valid, key=lambda h : h.index)

if __name__ == '__main__':
    assert stretch('abc0') == 'a107ff634856bb300138cac6568c0f24'
    x = solve('abc')
    x = solve('ihaygndm')
    print('-'*80)
    for i, y in enumerate(x):
        print(i, y)

    print('-'*80)
    print(x[64])

