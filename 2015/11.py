import string
import re

def next_password(password):
    """
    Build next valid password
    according to special rules
    """
    alphabet = string.ascii_lowercase
    nb = len(alphabet)
    limit = len(password)

    def _triplets(string):
        return set([string[c:c+3] for c in range(0, len(string)-2)])

    alpha_tri = _triplets(alphabet)

    def _increment(password):
        # Helper to increment a string
        # by one char
        alpha = list(alphabet)
        p = list(password)
        p.reverse()
        carry = 1
        out = []
        for c in p:
            value = alpha.index(c) + carry
            if value > nb - 1:
                carry = 1
            else:
                carry = 0
            out.append(alpha[value % nb])

        if len(out) > limit:
            raise Exception('too long')

        out.reverse()
        return ''.join(out)

    def _valid(password):
        # Helper to check if a password
        # is valid

        # Forbidden chars
        forbidden = set(['i', 'o', 'l'])
        if forbidden.intersection(list(password)):
            return False

        # At least 2 consecutive letters
        res = re.findall(r"(\w)\1", password)
        if not res or len(res) < 2:
            return False

        # Build triplets possible
        if not len(alpha_tri.intersection(_triplets(password))):
            return False

        return True

    # Search next valid
    password = _increment(password)
    while not _valid(password):
        password = _increment(password)

    return password

if __name__ == '__main__':
    print next_password('hepxcrrq')
    print next_password('hepxxyzz')
