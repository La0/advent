import re


def is_triangle(sides):
    total = sum(sides)
    for i in range(3):
        remaining = sides[i]
        if (total - remaining) <= remaining:
            return False
    return True


def solve(lines):
    grid = [map(int, re.findall('(\d+)', line)) for line in lines]
    triangles = []
    for i in range(len(grid)):
        x = i % 3
        y = (i / 3) * 3 # 3 by 3
        triangles.append([
            grid[y][x],
            grid[y+1][x],
            grid[y+2][x],
        ])

    return sum(map(is_triangle, triangles))

if __name__ == '__main__':
    with open('3.txt') as f:
        n = solve(f.readlines())
        print(n)
