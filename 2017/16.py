def dance(programs, steps):
    assert isinstance(programs, str)
    programs = list(programs)

    for step in steps.split(','):

        if step.startswith('s'):
            # Spin
            pos = int(step[1:])
            programs = programs[-pos:] + programs[:-pos]

        elif step.startswith('x'):
            # Exchange
            split = step.index('/')
            a = int(step[1:split])
            b = int(step[split+1:])
            programs[a], programs[b] = programs[b], programs[a]

        elif step.startswith('p'):
            # partner
            split = step.index('/')
            a = programs.index(step[1:split])
            b = programs.index(step[split+1:])
            programs[a], programs[b] = programs[b], programs[a]

    return ''.join(programs)

def loop_dance(loops, programs, steps):
    cache = {}
    for i in xrange(loops):

        # Check cache
        if programs in cache:
            programs = cache[programs]
            continue

        # New exec
        new_programs = dance(programs, steps)
        cache[programs] = new_programs
        programs = new_programs
    return programs


if __name__ == '__main__':
    assert dance('abcde', 's1,x3/4,pe/b') == 'baedc'
    assert loop_dance(2, 'abcde', 's1,x3/4,pe/b') == 'ceadb'

    programs = ''.join([chr(97+i) for i in range(16)])
    with open('16.txt') as f:
        steps = f.read().rstrip()
        print(dance(programs, steps))
        print(loop_dance(1000000000, programs, steps))
