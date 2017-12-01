def calc(digits):
    out = 0
    nb = len(digits)
    for i in range(nb):
        current = digits[i]
        next = digits[(i+1)%nb]
        if current == next:
            out += int(current)
    return out

def calc2(digits):
    out = 0
    nb = len(digits)
    offset = nb / 2
    for i in range(nb):
        current = digits[i]
        next = digits[(i+offset)%nb]
        if current == next:
            out += int(current)
    return out


if __name__ == '__main__':
    # part 1
    assert calc('1122') == 3
    assert calc('1111') == 4
    assert calc('1234') == 0
    assert calc('91212129') == 9
    print(calc(open('1.txt').read().rstrip()))

    # part 2
    assert calc2('1212') == 6
    assert calc2('1221') == 0
    assert calc2('123425') == 4
    assert calc2('123123') == 12
    assert calc2('12131415') == 4
    print(calc2(open('1.txt').read().rstrip()))

