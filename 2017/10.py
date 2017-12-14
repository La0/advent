from functools import reduce

def checksum(n, lengths, pos=0, skip=0, digits=None):
    if digits is None:
        digits = range(n)
    for length in lengths:
        assert length <= n

        # Reverse digits in a circular list
        for i in range(length / 2):
            src = (pos + length - i - 1) % n
            dest = (pos + i) % n
            digits[dest], digits[src] = digits[src], digits[dest]

        # move position
        pos += length + skip

        # increase skip
        skip += 1

    return digits[0] * digits[1], digits, pos, skip

def knot_hash(payload):
    assert isinstance(payload, str)

    # Build integer payload
    payload = map(ord, payload) + [17, 31, 73, 47, 23]

    # Iterate over hash
    pos, skip = 0, 0
    sparse = None
    for i in range(64):
        _, sparse, pos, skip = checksum(256, payload, pos, skip, sparse)

    # Calc dense hash
    dense = [
        reduce(lambda x, y: x ^ y, sparse[i:i+16])
        for i in range(0, 256, 16)
    ]
    out = ''.join(map(lambda x : str.format('{:02x}', x), dense))
    return out


if __name__ == '__main__':
    assert checksum(5, [3, 4, 1, 5])[0] == 12
    print(checksum(256, [225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110])[0])

    assert knot_hash('') == 'a2582a3a0e66e6e86e3812dcb672a272'
    assert knot_hash('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
    assert knot_hash('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
    assert knot_hash('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'
    print(knot_hash('225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110'))
