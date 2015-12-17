import itertools

def all_combinations(any_list):
    return itertools.chain.from_iterable(
            itertools.combinations(any_list, i + 1)
                    for i in xrange(2, len(any_list)))

def list_combinations(lines, target):
    containers = map(int, lines)
    combinations = all_combinations(containers)

    out = [(c, len(c)) for c in combinations if sum(c) == target]

    print 'Nb', len(out)

    m = min([x for _,x in out])
    print 'Min', m
    print 'Nb min', len([x for x,l in out if l == m])

    return


if __name__ == '__main__':
    target = 150
    with open('17.input', 'r') as f:
        list_combinations(f.readlines(), target)
