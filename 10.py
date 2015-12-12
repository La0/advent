import re
def look_and_say(seed, nb):
    """
    Iter LookAndSay op nb times
    from seed
    """
    def mutate(line):
        splits = [m.group(0) for m in re.finditer(r"(\d)\1*", line)]
        return ''.join(['%d%s' % (len(s), s[0]) for s in splits])

    for i in range(0, nb):
        seed = mutate(seed)

    return len(seed)

if __name__ == '__main__':
    print look_and_say('1321131112', 50)
