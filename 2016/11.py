import re
import copy
import itertools


regex_chips = re.compile(r'(\w+)-compatible microchip')
regex_gens = re.compile(r'(\w+) generator')

# possible moves:
# go up with 1..4
# go down with 1..4

def split(floor):
    # Split gens & chips from a floor
    assert isinstance(floor, list)
    return (
        # gens
        sorted([x[:2] for x in floor if x.endswith('g')]),
        # chips
        sorted([x[:2] for x in floor if x.endswith('m')])
    )

def check_state(state):
    # Check every floor doest not have
    # any chip without a generator
    # when there is a generator on the floor
    for floor in state:
        gens, chips = split(floor)
        if not gens or not chips:
            continue
        diff = set(chips).difference(gens)
        if len(diff) > 0:
            return False
    return True

def final_state(state):
    n = len(state)

    # Low floors must be empty
    for i in range(n-1):
        if len(state[i]) > 0:
            return False

    # Top floor must have only couples
    gens, chips = split(state[n-1])
    return gens == chips

def next_states(state, elevator):
    out = []
    n = len(state)

    items = state[elevator]
    if not items:
        return

    def _build_next(comb, next_elevator):
        ns = copy.deepcopy(state)
        # add to next floor
        ns[next_elevator] += comb
        # remove from current floor
        ns[elevator] = [x for x in ns[elevator] if x not in comb]

        ok = check_state(ns) and 'ok' or 'KO'
        print('{} comb {} on next elevator {}'.format(ok, ','.join(comb), next_elevator))
        display(ns, next_elevator)
        return (ns, next_elevator)

    # Produce all combinations possible
    # at most 2 items in elevator
    combs = [itertools.combinations(items, x+1) for x in range(2)]
    combs = list(itertools.chain.from_iterable(combs))

    for comb in combs:

        if elevator > 0:
            # Go Down
            out.append(_build_next(comb, elevator - 1))

        if elevator < n - 1:
            # Go up
            out.append(_build_next(comb, elevator + 1))

    return out

def display(state, elevator):
    # Helper
    dsp = ['{} {} {}'.format(i+1, i == elevator and 'E' or '.', ' '.join(fl)) for i, fl in enumerate(state)]
    dsp.reverse()
    print('\n'.join(dsp))

def run_tree(state, elevator=0, count=0):
    display(state, elevator)
    print('-' * 80, count)
    if not check_state(state):
        return

    if final_state(state):
        print('FINAL', count)
        return count

    # DEBUG
    if count >= 100:
        return 'stop'

    # Recursively browse through tree
    for next_state, next_elevator in next_states(state, elevator):
        out = run_tree(next_state, next_elevator, count+1)
        if out is not None:
            return out

def run(lines):
    # Parse input and build first state
    state = []
    for line in lines:
        chips = list(map(lambda x : x[:2].upper()+'m', regex_chips.findall(line)))
        gens = list(map(lambda x : x[:2].upper()+'g', regex_gens.findall(line)))
        state.append(chips+gens)

    # Search through tree
    return run_tree(state)

if __name__ == '__main__':
    with open('11.sample.txt') as f:
        solution = run(f.readlines())
        print(solution)
