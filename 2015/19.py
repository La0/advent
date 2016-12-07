import re
import random

class Machine(object):
    """
    Molecule creator !
    """
    def __init__(self, filename):
        regex = re.compile(r'^(\w+) => (\w+)\n$')

        # Load input
        self.replace = {}
        with open(filename, 'r') as f:
            for line in f.readlines():
                if line == '\n':
                    continue
                res = regex.match(line)
                if res:
                    a, b = res.groups()
                    self.replace[b] = a
                else:
                    self.target = line.replace('\n', '')

    def calibrate(self, source):
        """
        Find all molecules generated in one step
        """
        if source.count('e') > 1:
            return # optim

        calibrations = set()
        for atom, replace in self.replace.items():
            l = len(atom)

            for i in range(0, len(source) - l + 1):
                c = source[i:i+l]

                if c != atom:
                    continue

                s = list(source)
                s = s[:i] + [self.replace[atom], ] + s[i+len(atom):]
                out = ''.join(s)
                calibrations.add(out)


        return calibrations

    def build(self):
        """
        List all possible combinations to build target
        """
        all_steps = []

        def _search(source, steps):
            if not len(source):
                return
            if source == 'e':
                print 'FOUND!', steps
                all_steps.append(int(steps))
                return

            calib = self.calibrate(source)
            if not calib:
                return

            for c in calib:
                _search(c, steps+1)

        _search(self.target, 0) # start from electron
        return min(all_steps)

    def solve(self):
        """
        Try solving target by substituting all chars
        """
        keys = self.replace.keys()

        cpt = 0
        while self.target != 'e':
            random.shuffle(keys)
            for key in keys:
                replace = self.replace[key]
                self.target, n = re.subn(key, replace, self.target)
                if n > 0:
                    print key, replace, self.target
                cpt += n

        return cpt


if __name__ == '__main__':
    m = Machine('19.input')
    print m.solve()
