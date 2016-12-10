import re

regex_value = re.compile(r'value (\d+) goes to (\w+) (\d+)')
regex_gives = re.compile(r'bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)')


class Target(object):

    def __init__(self, type, id):
        self.type = type
        self.id = id
        self.values = []
        self.to_solve = []
        self.low = None
        self.high = None

    def __repr__(self):
        return '{} {} low={} high={}'.format(self.type, self.id, self.low, self.high)

    def solve(self):
        if self.low is not None and self.high is not None:
            return

        # Solve dependencies
        for t, from_bot in self.to_solve:
            from_bot.solve()
            if t == 'high':
                self.add(from_bot.high)
            elif t == 'low':
                self.add(from_bot.low)

        self.low = min(self.values)
        self.high = max(self.values)
        self.to_solve = []
        self.values = []

    def add(self, value):
        self.values.append(value)

    def set(self, value_type, from_bot):
        self.to_solve.append((value_type, from_bot))


def run(lines):
    targets = {
        'bot' : {},
        'output' : {},
    }

    def get(t, x):
        if x not in targets[t]:
            targets[t][x] = Target(t, x)
        return targets[t][x]

    for line in lines:
        # Parse value attribution
        out = regex_value.match(line)
        if out:
            data = out.groups()
            bot = get(data[1], int(data[2]))
            bot.add(int(data[0]))

        out = regex_gives.match(line)
        if out:
            data = out.groups()
            from_bot = get('bot', int(data[0]))

            # Low
            to_bot = get(data[1], int(data[2]))
            to_bot.set('low', from_bot)

            # High
            to_bot = get(data[3], int(data[4]))
            to_bot.set('high', from_bot)

    # Display outputs
    for cat, tt in targets.items():
        for o in tt.values():
            o.solve()
            print(o)


if __name__ == '__main__':
    with open('10.txt') as f:
        run(f.readlines())
