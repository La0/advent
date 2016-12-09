import re


def decompress(line):
    out = ''
    pos = 0
    line = line.replace(' ', '') # whitespaces ignored

    regex = re.compile(r'\((\d+)x(\d+)\)')

    while True:
        match = regex.search(line, pos)
        if match is None:
            out += line[pos:]
            break

        start, end = match.start(), match.end()

        # Add previous rest
        if start > 0:
            out += line[pos:start]

        # Decompress sequence
        nb_chars, times = map(int, match.groups())
        pos = end

        chars = line[pos:pos+nb_chars] * times
        out += chars
        pos += nb_chars

    return out


if __name__ == '__main__':
    assert decompress('ADVENT') == 'ADVENT'
    assert decompress('A(1x5)BC') == 'ABBBBBC'
    assert decompress('(3x3)XYZ') == 'XYZXYZXYZ'
    assert decompress('A(2x2)BCD(2x2)EFG') == 'ABCBCDEFEFG'
    assert decompress('(6x1)(1x3)A') == '(1x3)A'
    assert decompress('X(8x2)(3x3)ABCY') == 'X(3x3)ABC(3x3)ABCY'

    with open('9.txt') as f:
        out = decompress(f.read().replace('\n', ''))
        print(len(out))
