import re

class Circuit(object):
    wires = {}

    def read(self, line):
        regex = {
            r'^(\w+) -> (\w+)$' : self.init_signal,
            r'^(\w+) AND (\w+) -> (\w+)$' : self.op_and,
            r'^(\w+) OR (\w+) -> (\w+)$' : self.op_or,
            r'^(\w+) LSHIFT (\d+) -> (\w+)$' : self.op_lshift,
            r'^(\w+) RSHIFT (\d+) -> (\w+)$' : self.op_rshift,
            r'^NOT (\w+) -> (\w+)$' : self.op_not,
        }


        result = None
        for r,op in regex.items():
            # Find op
            res = re.search(r, line)
            if res is None:
                continue

            # Extract res
            groups = res.groups()
            result = groups[-1]
            self.wires[result] = (op, groups[0:-1])

        if result is None:
            raise Exception('Missing wire input from', line)

    def init_signal(self, signal):
        """
        Add a signal on a wire
        """
        print '=', signal
        return self.get(signal)

    def op_and(self, x, y):
        """
        res = x AND y
        """
        print x, '&', y
        return self.get(x) & self.get(y)

    def op_or(self, x, y):
        """
        res = x OR y
        """
        print x, '|', y
        return self.get(x) | self.get(y)

    def op_lshift(self, wire, val):
        """
        res = wire << val
        """
        print wire, '<<', val
        return self.get(wire) << int(val)

    def op_rshift(self, wire, val):
        """
        res = wire >> val
        """
        print wire, '>>', val
        return self.get(wire) >> int(val)

    def op_not(self, wire):
        """
        res = NOT wire
        """
        print '!', wire
        return ~ self.get(wire)

    def get(self, wire):

        # Direct value ?
        try:
            return int(wire) % 65536
        except ValueError:
            pass

        # Stored value ?
        val = self.wires[wire]
        if isinstance(val, int):
            return val % 65536

        # Recursively fetch & save wires values
        op, data = val
        result = op(*data) % 65536
        self.wires[wire] = result
        return result

    def run(self, target):
        # Run target wire
        self.wires[target] = self.get(target)

        # Final output
        for w in sorted(self.wires.keys()):
            val = self.wires[w]
            if not isinstance(val, int):
                continue
            if val <= 0:
                val = 65536 + val
            print '%s: %s' % (w, val)

if __name__ == '__main__':
    c = Circuit()
    with open('7.input', 'r') as f:
        for line in f.readlines():
            c.read(line.replace('\n', ''))
    c.run('a')
