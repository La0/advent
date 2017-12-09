import re
REGEX = re.compile(r'^(\w+) (inc|dec) ([\-\d]+) if (\w+) ([!=><]+) ([\-\d]+)', re.MULTILINE)

def max_register(lines):
    registers = {}
    ops = {
        'inc': lambda r,v : registers[r] + v,
        'dec': lambda r,v : registers[r] - v,
        '==': lambda r,v : registers[r] == v,
        '!=': lambda r,v : registers[r] != v,
        '>': lambda r,v : registers[r] > v,
        '<': lambda r,v : registers[r] < v,
        '>=': lambda r,v : registers[r] >= v,
        '<=': lambda r,v : registers[r] <= v,
    }
    max_value = 0
    for r, op, value, r2, op2, value2 in REGEX.findall(lines.read()):

        # Init registers
        if r not in registers:
            registers[r] = 0
        if r2 not in registers:
            registers[r2] = 0

        # Ran operation when constraint validates
        if ops[op2](r2, int(value2)):
            registers[r] = ops[op](r, int(value))

        # Save max value
        max_value = max(max_value, *registers.values())


    return max(registers.values()), max_value

if __name__ == '__main__':
    assert max_register(open('8.sample.txt')) == (1, 10)
    print(max_register(open('8.txt')))
