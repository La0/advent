import re

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

if __name__ == '__main__':
    limit = 2503
    speeds = []
    with open('14.input', 'r') as f:
        for line in f.readlines():
            speeds.append(calc_distance(line.replace('\n', ''), limit))

    print max(speeds)
