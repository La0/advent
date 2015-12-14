import re
from collections import namedtuple

regex = re.compile(r'^(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.$')

def calc_distance(line, target):
    """
    Calc the distance traveled
    after reaching target seconds
    """
    # Get data from line
    res = regex.match(line)
    if not res:
        raise Exception('Invalid input %s' % line)
    name, speed, speed_time, rest_time = res.groups()
    speed = int(speed)
    speed_time = int(speed_time)
    rest_time = int(rest_time)

    # Calc nb of period
    period = speed_time + rest_time
    nb = target / period
    last = min(target % period, speed_time) * speed

    # Calc distance traveled
    return nb * speed_time * speed + last

class Deer(object):
    def __init__(self, line):
        res = regex.match(line.replace('\n', ''))
        if not res:
            raise Exception('Invalid input %s' % line)
        self.name, self.speed, self.speed_time, self.rest_time = res.groups()
        self.speed = int(self.speed)
        self.speed_time = int(self.speed_time)
        self.rest_time = int(self.rest_time)
        self.distance = 0
        self.points = 0

    def __unicode__(self):
        return self.name

    def update(self, second):
        time = second % (self.speed_time + self.rest_time)
        if time < self.speed_time:
            self.distance += self.speed

    def lead(self):
        self.points += 1
        print self.name, self.distance, self.points


def calc_points(lines, target):
    """
    Calc points earned on lead per second
    """
    # Build deers
    deers = [Deer(line) for line in lines]

    for second in range(0, target):
        # Every second, update speed
        for deer in deers:
            deer.update(second)

        # Find leaders with best score
        top_dist = max([d.distance for d in deers])
        map(lambda x : x.lead(), [d for d in deers if d.distance == top_dist])

    # Output max points
    return max([d.points for d in deers])

if __name__ == '__main__':
    limit = 2503
    speeds = []
    with open('14.input', 'r') as f:
        # First half
        for line in f.readlines():
            speeds.append(calc_distance(line.replace('\n', ''), limit))
        print max(speeds)

        # Second half
        f.seek(0)
        print calc_points(f.readlines(), limit)
