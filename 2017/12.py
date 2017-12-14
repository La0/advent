import re
REGEX = re.compile(r'^(\d+) <-> ([\d,\s]+)\n')

def build_graph(path):
    # Build graph
    graph = {}
    for line in open(path).readlines():
        groups = REGEX.match(line).groups()
        graph[int(groups[0])] = map(int, groups[1].split(', '))
    return graph

# Browse graph from a starting point
def browse(graph, i, used):
    used += [i, ]
    for child in graph[i]:
        if child in used:
            continue
        browse(graph, child, used)

    return used

def count_programs(path):
    graph = build_graph(path)
    return len(browse(graph, 0, []))

def count_groups(path):
    graph = build_graph(path)
    nb = 0
    all_used = []
    for index in graph.keys():
        if index in all_used:
            continue

        all_used += browse(graph, index, [])
        nb += 1

    return nb


if __name__ == '__main__':
    assert count_programs('12.sample.txt') == 6
    print(count_programs('12.txt'))
    assert count_groups('12.sample.txt') == 2
    print(count_groups('12.txt'))
