
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

if __name__ == '__main__':
    #print is_nice('aaa')
    #aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
    #jchzalrnumimnmhp is naughty because it has no double letter.
    #haegwjzuvuyypxyu is naughty because it contains the string xy.
    #dvszwmarrgswjxmb

    with open('5.input', 'r') as f:
       print sum([is_nice(line.replace('\n', '')) for line in f.readlines()])
