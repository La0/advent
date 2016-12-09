import re


def decompress(line):
    if '(' not in line:
        return len(line)

    out = 0
    pos = 0
    line = line.replace(' ', '') # whitespaces ignored

    regex = re.compile(r'\((\d+)x(\d+)\)')

    while True:
        match = regex.search(line, pos)
        if match is None:
            out += len(line[pos:])
            break

        start, end = match.start(), match.end()

        # Add previous rest
        if start > 0:
            out += len(line[pos:start])

        # Decompress sequence
        nb_chars, times = map(int, match.groups())
        pos = end

        chars = line[pos:pos+nb_chars]
        nb = decompress(chars)
        out += nb * times
        pos += nb_chars

    return out


if __name__ == '__main__':
    assert decompress('ADVENT') == 6
    assert decompress('A(1x5)BC') == 7
    assert decompress('(3x3)XYZ') == 9
    assert decompress('A(2x2)BCD(2x2)EFG') == len('ABCBCDEFEFG')
    assert decompress('(6x1)(1x3)A') == 3
    assert decompress('X(8x2)(3x3)ABCY') == len('XABCABCABCABCABCABCY')
    assert decompress('(27x12)(20x12)(13x14)(7x10)(1x12)A') == 241920
    assert decompress('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN') == 445

    with open('9.txt') as f:
        print('run..')
        out = decompress(f.read().replace('\n', ''))
        print(out)
