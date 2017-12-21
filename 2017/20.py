import re
from collections import Counter
REGEX = re.compile('p=<([-\d]+),([-\d]+),([-\d]+)>, v=<([-\d]+),([-\d]+),([-\d]+)>, a=<([-\d]+),([-\d]+),([-\d]+)>')

class Particle(object):

    def __init__(self, index, line):
        self.index = index

        # Parse
        out = REGEX.search(line)
        assert out is not None
        self.px, self.py, self.pz, self.vx, self.vy, self.vz, self.ax, self.ay, self.az = map(int, out.groups())

    def tick(self):
        self.vx += self.ax
        self.vy += self.ay
        self.vz += self.az
        self.px += self.vx
        self.py += self.vy
        self.pz += self.vz

    def distance(self, x, y, z):
        return sum([
            abs(self.px - x),
            abs(self.py - y),
            abs(self.pz - z),
        ])

    @staticmethod
    def load(path):
        with open(path) as f:
            return [
                Particle(i, line)
                for i, line in enumerate(f.readlines())
            ]


def run(particles, n=100, collision=False):
    close = []
    while True:
        distances = []
        positions = []
        for p in particles:
            p.tick()
            distances.append((p.index, p.distance(0, 0, 0)))
            positions.append((p.px, p.py, p.pz))

        if collision:
            # Find and clean collisions
            for k, v in Counter(positions).items():
                if v == 1:
                    continue
                particles = filter(lambda p : (p.px, p.py, p.pz) != k, particles)

        distances = sorted(distances, key=lambda x : x[1])
        current = distances[0][0]
        close.append(current)
        if len(close) > n and all([c == current for c in close[-n:]]):
            return collision and len(particles) or current

if __name__ == '__main__':
    sample = Particle.load('20.sample.txt')
    assert run(sample) == 0

    # Part 1
    real = Particle.load('20.txt')
    print(run(real, 1000))

    # Part 2
    sample = Particle.load('20.sample2.txt')
    assert run(sample, collision=True) == 1
    print(run(real, 1000, collision=True))
