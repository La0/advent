import re
def search_shortest(lines):
    """
    Search shortest travel distance
    for passing in every point
    """

    cities = {}

    # List places
    for line in lines:
        res = re.search(r'(\w+) to (\w+) = (\d+)', line)
        if not res:
            raise Exception('Invalid line %s' % line)

        start, end, distance = res.groups()

        if start not in cities:
            cities[start] = {}
        if end not in cities:
            cities[end] = {}

        cities[start][end] = int(distance)
        cities[end][start] = int(distance)

    costs = {}
    def _build_travel(parts, limit, travel, level=0, best_cost=10000):
        if level >= limit:

            # Find best cost
            cost = sum([cities[travel[i]][travel[i+1]] for i in range(0, len(travel) - 1)])
            if cost in costs:
                costs[cost].append(list(travel))
            else:
                costs[cost] = [list(travel), ]
            return

        for i, p in enumerate(parts):
            if p is None:
                continue
            parts[i] = None

            travel[level] = p

            _build_travel(parts, limit, travel, level+1, best_cost);
            parts[i] = p

    _build_travel(sorted(cities.keys()), len(cities), [None, ]* len(cities))

    best = max(costs.keys())
    print 'BEST', best
    for t in costs[best]:
        print t

if __name__ == '__main__':
    with open('9.input', 'r') as f:
        search_shortest(f.readlines())
