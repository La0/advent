import re

def calc_length(line):


    # Code
    total_code = len(line)

    # In memory
    # * kill quotes
    line = line[1:-1]
    line = r''.join(line)

    print line

    # * kill utf-8 hex code
    line = re.sub(r'\\x([0-9a-fA-F]{2})', 'x', line)

    # * kill escaped chars
    line = line.replace(r'\"', '"')
    line = line.replace(r'\\', '\\')

    total_memory = len(line)

    print line

    print ' > code', total_code
    print ' > memory', total_memory
    return total_code - total_memory

if __name__ == '__main__':
    total = 0
    with open('8.input', 'rU') as f:
        line = []

        # Read char by char
        while f:
            c  = f.read(1)
            if c in ('\n', ''):
                if c == '':
                    break
                else:
                    total += calc_length(line)
                    line = []
                    continue
            line.append(c)

    print 'Total', total
