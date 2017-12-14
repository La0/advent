def on_top(step, r):
    total = (r * 2) - 2
    return step % total == 0

def build_conf(path):
    return dict([
        map(int, line.rstrip().split(': '))
        for line in open(path).readlines()
    ])


def severity(path):
    conf = build_conf(path)
    return sum([
        step * conf[step]
        for step in range(max(conf.keys()) + 1)
        if step in conf and on_top(step, conf[step])
    ])

def delay(path):
    delay = 10
    conf = build_conf(path)
    while True:

        caught = False
        for step in range(max(conf.keys()) + 1):
            if step in conf and on_top(delay + step, conf[step]):
                # got caught
                caught = True
                break

        if not caught:
            return delay
        delay += 1


if __name__ == '__main__':
    assert severity('13.sample.txt') == 24
    print(severity('13.txt'))
    assert delay('13.sample.txt') == 10
    print(delay('13.txt'))
