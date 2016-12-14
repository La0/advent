import hashlib
from collections import namedtuple

Hash = namedtuple('Hash', 'index, hash, char')

def is_triplet(x):
    chars = '01234567890abcdef'
    for c in chars:
        if c*3 in x:
            return c

def is_five(x, c):
    return c*5 in x

def solve(salt):
    valid = []
    running = []

    i = 0
    while len(valid) < 64:
        contents = '{}{}'.format(salt, i)
        h = hashlib.md5(contents).hexdigest()
        current = Hash(i, h, is_triplet(h))

        for index, run in enumerate(running):
            # still running ?
            if current.index - run.index > 1000:
                del running[index]
                continue

            # has match ?
            if is_five(current.hash, run.char):
                valid.append(run)

        # Triplet ?
        if current.char is not None:
            running.append(current)

        i += 1

    return sorted(valid, key=lambda h : h.index)

if __name__ == '__main__':
    #x = solve('abc')
    x = solve('ihaygndm')
    print(x[-1])
