import re

class Machine(object):
    """
    Molecule creator !
    """
    def __init__(self, filename):
        regex = re.compile(r'^(\w+) => (\w+)\n$')
        self.calibrations = set()

        # Load input
        self.replace = {}
        with open(filename, 'r') as f:
            for line in f.readlines():
                if line == '\n':
                    continue
                res = regex.match(line)
                if res:
                    a, b = res.groups()
                    if a not in self.replace:
                        self.replace[a] = []
                    self.replace[a].append(b)
                else:
                    self.start = line.replace('\n', '')

    def calibrate(self):
        """
        Find all molecules generated in one step
        """
        for atom, replace in self.replace.items():
            l = len(atom)

            for i in range(0, len(self.start) - l + 1):
                c = self.start[i:i+l]

                if c != atom:
                    continue

                for r in replace:
                    self.add_replacement(i, atom, r)

        return len(self.calibrations)

    def add_replacement(self, pos, src, dest):
        s = list(self.start)
        s = s[:pos] + [dest, ] + s[pos+len(src):]
        out = ''.join(s)
        print '#%d %s => %s = %s' % (pos, src, dest, out)
        self.calibrations.add(out)



if __name__ == '__main__':
    m = Machine('19.test')
    m = Machine('19.input')
    print m.calibrate()
