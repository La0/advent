import re


def solve(lines):
    out = len(lines)
    for line in lines:
        sides = map(int, re.findall('(\d+)', line))
        total = sum(sides)
        for i in range(3):
            remaining = sides[i]
            if (total - remaining) <= remaining:
                out -= 1
                break

    return out

if __name__ == '__main__':
    with open('3.txt') as f:
        n = solve(f.readlines())
        print(n)
