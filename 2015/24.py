import itertools
import operator

def find_packages(filename):

    # Load weights
    with open(filename, 'r') as f:
        weights = map(int, f.readlines())

    # Build smallest triplets
    # Find all possible groups
    target = sum(weights) / 4 # 4 equal groups
    print 'Target', target
    for i in range(2, len(weights)):
        groups = [g for g in itertools.combinations(weights, i) if sum(g) == target]
        if groups:
            break

    triplets = []
    for g in groups:
        qe = reduce(operator.mul, g)
        nb = len(g)
        triplets.append((g, nb, qe))

    triplets = sorted(triplets, key=lambda t : (t[1], t[2]))

    best = triplets[0]
    print best

    return best[2]

if __name__ == '__main__':
    print find_packages('24.test')
    print find_packages('24.input')
