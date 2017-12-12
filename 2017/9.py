def cleanup(line):
    '''
    Remove all garbage from line input
    '''
    out = ''
    garbage = False
    canceled = False
    nb = 0
    for i, c in enumerate(line):

        # Skip any char
        if i > 0 and line[i-1] == '!' and not canceled:
            canceled = True
            continue

        # Good chars
        if not garbage and c != '<':
            out += c
            continue

        # Stoping garbage
        if garbage and c == '>':
            garbage = False
            continue

        # reset canceled
        canceled = False

        # count good chars in garbage
        if garbage and not canceled and c != '!':
            nb += 1

        # Starting garbage
        if not garbage and c == '<':
            garbage = True

    return out, nb

def calc_score(line, level=1):
    '''
    List available groups
    '''
    line, _ = cleanup(line)
    opened = 0
    start = 0
    for i, c in enumerate(line):
        if c == '{':
            # open new group
            if opened == 0:
                start = i
            opened += 1

        elif c == '}':
            if opened == 1:
                # close last group
                return level + calc_score(line[start+1:i], level+1) + calc_score(line[i+1:], level)

            opened -= 1

    return 0

if __name__ == '__main__':
    assert cleanup('<>') == ('', 0)
    assert cleanup('<random characters>') == ('', 17)
    assert cleanup('<<<<>') == ('', 3)
    assert cleanup('<{!>}>') == ('', 2)
    assert cleanup('<!!>') == ('', 0)
    assert cleanup('<!!!>>') == ('', 0)
    assert cleanup('<{o"i!a,<{i<a>') == ('', 10)
    assert cleanup('{{<!!>},{<!!>},{<!!>},{<!!>}}') == ('{{},{},{},{}}', 0)
    assert calc_score('{}') == 1
    assert calc_score('{{{}}}') == 6
    assert calc_score('{{},{}}') == 5
    assert calc_score('{{{},{},{{}}}}') == 16
    assert calc_score('{<a>,<a>,<a>,<a>}') == 1
    assert calc_score('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9
    assert calc_score('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9
    assert calc_score('{{<a!>},{<a!>},{<a!>},{<ab>}},') == 3

    with open('9.txt') as f:
        data = f.read().rstrip()
        print(calc_score(data))
        print(cleanup(data)[1])


