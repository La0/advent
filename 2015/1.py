floors = {
    ')' : -1,
    '(' : 1,
}

def calc_floor(line):
    """
    Start on floor 0
    An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.
    """
    return sum([floors.get(c, 0) for c in line])

def find_basement(line):
    """
    Same rules, find first position at -1
    """
    floor = 0
    for i, c in enumerate(line):
        floor += floors.get(c, 0)
        if floor == -1:
            return i+1

if __name__ == '__main__':
    with open('1.input', 'r') as f:
        print find_basement(f.read())
