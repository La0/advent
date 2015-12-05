def calc_floor(line):
    """
    Start on floor 0
    An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.
    """
    floors = {
        ')' : -1,
        '(' : 1,
    }
    return sum([floors.get(c, 0) for c in line])

if __name__ == '__main__':
    with open('1.input', 'r') as f:
        print calc_floor(f.read())
