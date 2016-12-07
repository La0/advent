
def is_nice(line):
    """
    Check a line is nice:
        It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
        It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
        It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
    """
    print line
    vowels = ('a', 'e', 'i', 'o', 'u')
    forbidden = ('ab', 'cd', 'pq', 'xy')

    # Count vowels
    vowels_used = [c for c in line if c in vowels]
    print 'vowels', vowels_used
    if len(vowels_used) < 3:
        return False

    # Loop on couples
    twice = False
    for i,c in enumerate(line[0:-1]):
        nc = line[i+1]
        if nc == c:
            twice = True
            print 'Twice', twice, nc,c
        if c+nc in forbidden:
            print 'Forbidden', c+nc
            return False


    return twice

def is_nice_2(line):
    """
    It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
    """

    # All couples
    couples = [c+line[i+1] for i,c in enumerate(line[0:-1])]

    # Doubles
    doubles = set([c for c in couples if couples.count(c) > 1])
    if not doubles:
        return False

    # Calc position difference in doubles
    for d in doubles:
        indexes = [i for i,c in enumerate(couples) if c == d]
        if max(indexes) - min(indexes) <= 1:
            return False

    # All triplets
    triplets = [line[i:i+3] for i,c in enumerate(line[0:-2])]
    for a,b,c in triplets:
        if a == c:
            return True

    return False



if __name__ == '__main__':
    print is_nice_2('qjhvhtzxzqqjkmpb')
    print is_nice_2('xxyxx')
    print is_nice_2('aaa')
    #aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
    #jchzalrnumimnmhp is naughty because it has no double letter.
    #haegwjzuvuyypxyu is naughty because it contains the string xy.
    #dvszwmarrgswjxmb

    with open('5.input', 'r') as f:
       print sum([is_nice_2(line.replace('\n', '')) for line in f.readlines()])
