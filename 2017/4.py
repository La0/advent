from collections import Counter

def is_valid(phrase):
    words = phrase.split(' ')
    c = Counter(words)
    return c.most_common()[0][1] == 1

def is_valid2(phrase):
    words = [
        ''.join(sorted(w))
        for w in phrase.split(' ')
    ]

    c = Counter(words)
    return c.most_common()[0][1] == 1

if __name__ == '__main__':
    assert is_valid('aa bb cc dd ee')
    assert not is_valid('aa bb cc dd aa')
    assert is_valid('aa bb cc dd aaa')

    with open('4.txt') as f:
        valids = [
            is_valid(line.rstrip())
            for line in f.readlines()
        ]
        print(sum(valids))

    assert is_valid2('abcde fghij')
    assert not is_valid2('abcde xyz ecdab')
    assert is_valid2('a ab abc abd abf abj')
    assert is_valid2('iiii oiii ooii oooi oooo')
    assert not is_valid2('oiii ioii iioi iiio')

    with open('4.txt') as f:
        valids = [
            is_valid2(line.rstrip())
            for line in f.readlines()
        ]
        print(sum(valids))
