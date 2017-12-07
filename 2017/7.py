import re
import collections

Tower = collections.namedtuple('Tower', 'name, weight, children')

regex = re.compile('^(\w+) \((\d+)\)(?: -> ([\w\s,]+))?$')



def build_graph(body):
    out = {}
    for line in body:
        match = regex.search(line.rstrip())
        assert match is not None
        name, weight, children = match.groups()
        t = Tower(
            name,
            int(weight),
            children and children.split(', ') or []
        )
        out[t.name] = t

    return out

def find_parent(graph):
    # everyone can be the parent at first
    candidates = graph.keys()

    # List all children possible
    all_children = [
        c
        for tower in graph.values()
        for c in tower.children
    ]
    remains = set(candidates).difference(all_children)
    assert len(remains) == 1
    return remains.pop()

def balance(graph):

    def _calc_weight(name):
        assert isinstance(name, str)
        elt = graph[name]
        return elt.weight + sum([
            _calc_weight(child)
            for child in elt.children
        ])

    def is_balanced(name):
        elt = graph[name]
        weights = [
            _calc_weight(c)
            for c in elt.children
        ]
        return len(set(weights)) != 2

    def _fix(elt):
        weights = {
            c: _calc_weight(c)
            for c in elt.children
        }

        values = collections.Counter(weights.values()).most_common()
        assert len(values) != 1
        print('UNBALANCE', elt, weights)
        good = values[0][0]
        bad = values[-1][0]
        offset = good - bad
        print('offset', offset)
        inverse = dict(zip(weights.values(), weights.keys()))
        bad_elt = graph[inverse[bad]]
        return bad_elt.weight + offset

    def _find(name):
        elt = graph[name]
        if not elt.children:
            return 0

        if not is_balanced(name):
            childs_balanced = all([
                is_balanced(c)
                for c in elt.children
            ])
            if childs_balanced:
                # calc offset
                return _fix(elt)

        return sum([
            _find(c)
            for c in elt.children
        ])

    root = find_parent(graph)
    return _find(root)

if __name__ == '__main__':
    graph_sample = build_graph(open('7.sample.txt'))
    graph = build_graph(open('7.txt'))

    assert find_parent(graph_sample) == 'tknk'
    print(find_parent(graph))

    assert balance(graph_sample) == 60
    print(balance(graph))
