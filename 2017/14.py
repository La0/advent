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

# New code here !

def build_hashes(payload):

    def hash2bin(h):
        return ''.join([
            bin(int(h[x:x+2], 16))[2:].zfill(8)
            for x in range(0, len(h), 2)
        ])

    return [
        hash2bin(knot_hash('{}-{}'.format(payload, i)))
        for i in range(128)
    ]

def actives(payload):
    return [
        (x, y)
        for y, h in enumerate(build_hashes(payload))
        for x, b in enumerate(h)
        if b == '1'
    ]

def groups(payload):
    # List all active positions
    all_actives = actives(payload)
    groups = {}

    def neighbors(x, y):
        return [
            (x+i, y+j)
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]
            if (x+i, y+j) in all_actives
        ]

    for n, pos in enumerate(all_actives):

        n_groups = [
            groups[n]
            for n in neighbors(*pos)
            if n in groups
        ]

        if n_groups:
            # Merge into new group
            for k, g in groups.items():
                if g in n_groups:
                    groups[k] = n

        # Apply to position
        groups[pos] = n

    return len(set(groups.values()))

if __name__ == '__main__':
    print(len(actives('uugsqrei')))
    print(groups('uugsqrei'))
