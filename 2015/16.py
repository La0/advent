import re

detected = {
    'children' : 3,
    'cats' : 7,
    'samoyeds' : 2,
    'pomeranians' : 3,
    'akitas' : 0,
    'vizslas' : 0,
    'goldfish' : 5,
    'trees' : 3,
    'cars' : 2,
    'perfumes' : 1,
}

def find_sue(lines):
    aunts = {}

    # Extract data about all aunts
    regex = re.compile(r'^Sue (\d+): (.*)\n$')
    regex_props = re.compile(r'(\w+): (\d+)')
    for line in lines:
        res = regex.match(line)
        name, properties = res.groups()
        aunts[int(name)] = dict(map(lambda x : (x[0],int(x[1])),  regex_props.findall(properties)))


    # Find closest aunt
    best_distance = 1000
    for aunt, props in aunts.items():

        # Calc distance
        distance = 0
        for k,v in props.items():
            value = detected[k]
            if k in ('cats', 'trees') and v > value:
                continue
            if k in ('pomeranians', 'goldfish') and v < value:
                continue
            distance += abs(v - value)

        # Find min distance
        best_distance = min(distance, best_distance)
        if distance == best_distance:
            print aunt, props, distance

if __name__ == '__main__':
    with open('16.input', 'r') as f:
        find_sue(f.readlines())
