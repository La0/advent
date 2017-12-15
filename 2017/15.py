def int2bin(number):
    out = bin(number)[2:]
    return ('0' * (32 - len(out))) + out


class Generator(object):
    def __init__(self, factor, start):
        self.factor = factor
        self.previous = start
        self.multiple = None

    def next(self):
        def _next():
            self.previous = (self.previous * self.factor) % 2147483647
            return self.previous

        if self.multiple:
            # Part 2
            while True:
                value = _next()
                if value % self.multiple == 0:
                    return int2bin(value)

        # Part 1
        return int2bin(_next())

def count(n, genA, genB):
    nb = 0
    for i in xrange(n):
        a = genA.next()
        b = genB.next()
        if a[16:] == b[16:]:
            nb += 1
    return nb

if __name__ == '__main__':
    assert int2bin(1092455) == '00000000000100001010101101100111'
    assert int2bin(430625591) == '00011001101010101101001100110111'
    A = Generator(16807, 65)
    B = Generator(48271, 8921)
    assert count(5, A, B) == 1

    A.multiple = 4
    B.multiple = 8
    assert count(1056, A, B) == 1

    # My values
    A = Generator(16807, 722)
    B = Generator(48271, 354)

    # Part 1
    print(count(40*1000*1000, A, B))

    # Part 2
    A.multiple = 4
    B.multiple = 8
    print(count(5*1000*1000, A, B))
