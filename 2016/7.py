import re

def is_abba(line):
    for i in range(len(line) - 3):
        abba = line[i:i+4]
        if abba[0] == abba[3] and abba[1] == abba[2] and abba[0] != abba[1]:
            return True
    return False


def is_tls(address):
    # Split parts
    hypernets = re.findall(r'\[(\w+)\]', address)
    rest = re.split('\[\w+\]', address)

    # Need an abba in rest
    if True not in map(is_abba, rest):
        return False

    # No abba in hypernets
    if True in map(is_abba, hypernets):
        return False

    return True


if __name__ == '__main__':
    assert is_tls('abba[mnop]qrst')
    assert not is_tls('abcd[bddb]xyyx')
    assert not is_tls('aaaa[qwer]tyui')
    assert is_tls('ioxxoj[asdfgh]zxcvbn')

    with open('7.txt') as f:
        x = sum(map(is_tls, f.readlines()))
        print(x)
