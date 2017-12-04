import re
regex = re.compile(r'(\d+)')

def checksum(text):
    csum = 0
    for line in text.split('\n'):
        numbers = list(map(int, regex.findall(line)))
        if not numbers:
            continue
        csum += max(numbers) - min(numbers)
    return csum

def checksum2(text):
    csum = 0
    for line in text.split('\n'):
        numbers = list(map(int, regex.findall(line)))
        if not numbers:
            continue

        for x in numbers:
            for y in numbers:
                if x <= y:
                    continue

                if x % y == 0:
                    csum += x / y
                    break
    return csum


if __name__ == '__main__':
    test = '''5 1 9 5
    7 5 3
    2 4 6 8'''
    assert checksum(test) == 18
    print(checksum(open('2.txt').read()))

    test2 = '''5 9 2 8
    9 4 7 3
    3 8 6 5
    '''
    assert checksum2(test2) == 9
    print(checksum2(open('2.txt').read()))
