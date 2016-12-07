def solve(line):
    steps = line.split(', ')
    locations = []

    directions = (
        (1, 0),
        (0, -1),
        (-1, 0),
        (0, 1),
    )

    x, y = 0, 0
    index = 0
    for step in steps:
        direction = step[0]
        length = int(step[1:])

        if direction == 'R':
            index = (index + 1) % 4
        else:
            index = (index - 1) % 4

        vx, vy = directions[index]

        for i in range(length):
            pos = (x + vx * (i+1), y + vy * (i+1))
            if pos in locations:
                return abs(pos[0]) + abs(pos[1])
            locations.append(pos)

        x += vx * length
        y += vy * length

    return abs(x) + abs(y)


if __name__ == '__main__':

    x = solve('L1, L3, L5, L3, R1, L4, L5, R1, R3, L5, R1, L3, L2, L3, R2, R2, L3, L3, R1, L2, R1, L3, L2, R4, R2, L5, R4, L5, R4, L2, R3, L2, R4, R1, L5, L4, R1, L2, R3, R1, R2, L4, R1, L2, R3, L2, L3, R5, L192, R4, L5, R4, L1, R4, L4, R2, L5, R45, L2, L5, R4, R5, L3, R5, R77, R2, R5, L5, R1, R4, L4, L4, R2, L4, L1, R191, R1, L1, L2, L2, L4, L3, R1, L3, R1, R5, R3, L1, L4, L2, L3, L1, L1, R5, L4, R1, L3, R1, L2, R1, R4, R5, L4, L2, R4, R5, L1, L2, R3, L4, R2, R2, R3, L2, L3, L5, R3, R1, L4, L3, R4, R2, R2, R2, R1, L4, R4, R1, R2, R1, L2, L2, R4, L1, L2, R3, L3, L5, L4, R4, L3, L1, L5, L3, L5, R5, L5, L4, L2, R1, L2, L4, L2, L4, L1, R4, R4, R5, R1, L4, R2, L4, L2, L4, R2, L4, L1, L2, R1, R4, R3, R2, R2, R5, L1, L2')
    print(x)
