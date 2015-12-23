import re

def run_payload(filename):
    payload = []
    registers = {
        'a' : 0,
        'b' : 0,
    }

    # Load instructions
    ins_re = re.compile(r'^(\w+) ([\w\-\+\d]+)$')
    ins_cond = re.compile(r'^(\w+) (\w), ([\w\-\+\d]+)$')
    with open(filename, 'r') as f:
        for line in f.readlines():
            res = ins_re.match(line)
            if res:
                a, b = res.groups()
                try:
                    payload.append((a, int(b)))
                except:
                    payload.append((a, b))
            else:
                res = ins_cond.match(line)
                if res:
                    a, b, c = res.groups()
                    payload.append((a, b, int(c)))

    # Run instructions
    cursor = 0
    while 0 <= cursor < len(payload):
        line = payload[cursor]
        ins = line[0]
        print ins

        if ins == 'hlf':
            # Half register
            registers[line[1]] /= 2
            cursor += 1
        elif ins == 'tpl':
            # Triple register
            registers[line[1]] *= 3
            cursor += 1
        elif ins == 'inc':
            # Increment register
            registers[line[1]] += 1
            cursor += 1
        elif ins == 'jmp':
            # Relative jump
            cursor += line[1]
        elif ins == 'jie':
            # Relative jump, if even
            if registers[line[1]] % 2 == 0:
                cursor += line[2]
            else:
                cursor += 1
        elif ins == 'jio':
            # Relative jump, if one
            if registers[line[1]] == 1:
                cursor += line[2]
            else:
                cursor += 1

    return registers

if __name__ == '__main__':
    print run_payload('23.input')
