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

def calc_encoded(line):
    # Code
    total_code = len(line)

    # Encode the line
    line = r''.join(line)
    print line
    line = line.replace('\\', r'\\')

    # * utf8
    line = re.sub(r'\\x([0-9a-fA-F]{2})', r'\\x\1', line)

    # * quotes
    line = line.replace('"', r'\"')

    # Add enclosing quotes
    line = '"' + line + '"'

    total_encoded = len(line)
    print line
    print 'code', total_code
    print 'encoded', total_encoded

    return total_encoded - total_code

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
                    total += calc_encoded(line)
                    line = []
                    continue
            line.append(c)

    print 'Total', total
