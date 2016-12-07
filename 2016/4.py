import re
from collections import Counter

regex = re.compile(r'([\w\-]+)-(\d+)\[(\w+)\]')

def parse(line):
    return regex.match(line).groups()

def is_room(line):
    name, sector_id, checksum = parse(line)

    count = Counter(name.replace('-', ''))

    def _cmp(x, y):
        cx, nx = x
        cy, ny = y
        if nx == ny:
            return cx > cy and 1 or -1
        return nx < ny and 1 or -1

    chars = count.items()
    chars.sort(cmp=_cmp)
    check = ''.join([c[0] for c in chars[:5]])

    return check == checksum

def decrypt(line):
    name, sector_id, _ = parse(line)
    rot = int(sector_id) % 26
    def _rot(char):
        if char == '-':
            return ' '
        return chr((((ord(char) + rot) - 97) % 26) + 97)
    return ''.join(map(_rot, name)), sector_id

def calc_sum(lines):
    return sum([int(parse(line)[1]) for line in lines if is_room(line)])

def display(lines):
    for line in lines:
        if not is_room(line):
            continue
        name, sector = decrypt(line)
        if 'north' in name:
            print(name, sector)


if __name__ == '__main__':
    assert is_room('aaaaa-bbb-z-y-x-123[abxyz]')
    assert is_room('a-b-c-d-e-f-g-h-987[abcde]')
    assert is_room('not-a-real-room-404[oarel]')
    assert not is_room('totally-real-room-200[decoy]')
    with open('4.txt') as f:
        display(f.readlines())
