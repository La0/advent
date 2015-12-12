import json

def sum_json(filename):
    """
    Sum every number in a json file
    """

    def _count(data):
        if isinstance(data, int):
            return data

        if isinstance(data, list):
            return sum(map(_count, data))

        if isinstance(data, dict):
            return sum(map(_count, data.keys())) + sum(map(_count, data.values()))

        return 0

    with open(filename, 'r') as f:
        return _count(json.load(f))

if __name__ == '__main__':
    print sum_json('12.input')
