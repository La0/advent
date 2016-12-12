import re

registers = {}

def get(x):
    # Get value from register or cast to int
    try:
        return int(x)
    except ValueError:
        if x in registers:
            return registers[x]
        else:
            return 0

def inc(x):
    registers[x] += 1
    return 1

def dec(x):
    registers[x] -= 1
    return 1

def cpy(x, y):
    registers[y] = get(x)
    return 1

def jnz(x, y):
    return get(x) != 0 and int(y) or 1

ops = {
    re.compile(r'inc (\w+)') : inc,
    re.compile(r'dec (\w+)') : dec,
    re.compile(r'cpy (\w+) (\w+)') : cpy,
    re.compile(r'jnz (\w+) ([\d\-]+)') : jnz,
}

def run(instructions):
    cursor = 0
    registers['c'] = 1 # part 2
    while cursor >= 0 and cursor < len(instructions):
        line = instructions[cursor]
        print('cursor={} {} {}'.format(cursor, registers, line.replace('\n', '')))
        for regex, op in ops.items():
            match = regex.match(line)
            if match:
                cursor += op(*match.groups())
                break

    # Display registers
    for k,v in registers.items():
        print('Register {}={}'.format(k, v))

if __name__ == '__main__':
    with open('12.txt') as f:
        run(f.readlines())
