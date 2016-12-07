import itertools
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

def get_aba(line):
    out = []
    for i in range(len(line) - 2):
        aba = line[i:i+3]
        if aba[0] == aba[2] and aba[0] != aba[1]:
            out.append(aba)
    return out

def has_bab(line, aba):
    bab = aba[1] + aba[0] + aba[1]
    return bab in line

def is_ssl(address):
    # Split parts
    hypernets = re.findall(r'\[(\w+)\]', address)
    supernets = re.split('\[\w+\]', address)

    abas = sum(map(get_aba, supernets), [])
    if not abas:
        return False

    out = [
        has_bab(h, aba)
        for h, aba in itertools.product(hypernets, abas)
    ]
    return True in out


if __name__ == '__main__':
    assert is_tls('abba[mnop]qrst')
    assert not is_tls('abcd[bddb]xyyx')
    assert not is_tls('aaaa[qwer]tyui')
    assert is_tls('ioxxoj[asdfgh]zxcvbn')

    with open('7.txt') as f:
        x = sum(map(is_tls, f.readlines()))
        #print(x)

    assert is_ssl('aba[bab]xyz')
    assert not is_ssl('xyx[xyx]xyx')
    assert is_ssl('aaa[kek]eke')
    assert is_ssl('zazbz[bzb]cdb')

    with open('7.txt') as f:
        x = sum(map(is_ssl, f.readlines()))
        print(x)
