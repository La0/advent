from collections import Counter

def solve(lines):
    counts = map(Counter, zip(*[l.replace('\n', '') for l in lines]))
    return ''.join([c.most_common()[0][0] for c in counts])


if __name__ == '__main__':
    with open('6.txt') as f:
        x = solve(f.readlines())
        print(x)
