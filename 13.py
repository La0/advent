import re
def calc_happiness(lines):
    """
    Calc max happiness change
    for passing in every point
    """

    people = {}

    # List people links
    for line in lines:
        res = re.search(r'^(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).$', line)
        if not res:
            raise Exception('Invalid line %s' % line)

        # Calc score
        a, mod, change, b = res.groups()
        score = int(change)
        score *= mod == 'gain' and 1 or -1

        # Store 2 way link
        if a not in people:
            people[a] = {}

        people[a][b] = score

    from pprint import pprint
    pprint(people)

    costs = {}
    def _build_seating(parts, limit, seating, level=0, best_cost=10000):
        if level >= limit:

            # Find best cost
            nb = len(seating)
            cost = sum([
                people[seating[i]][seating[(i+1)%nb]] + \
                people[seating[(i+1)%nb]][seating[i]] \
                for i in range(0, nb)])
            if cost in costs:
                costs[cost].append(list(seating))
            else:
                costs[cost] = [list(seating), ]
            return

        for i, p in enumerate(parts):
            if p is None:
                continue
            parts[i] = None

            seating[level] = p

            _build_seating(parts, limit, seating, level+1, best_cost);
            parts[i] = p

    _build_seating(sorted(people.keys()), len(people), [None, ]* len(people))

    best = max(costs.keys())
    print 'BEST', best
    for t in costs[best]:
        print t

if __name__ == '__main__':
    with open('13.input', 'r') as f:
        calc_happiness(f.readlines())
