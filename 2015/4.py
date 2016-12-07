import hashlib

def mine(secret, nb):
    """
    Find md5 hash with nb zeroes
    including secret
    """
    i = 1
    while True:
        s = secret + str(i)
        h = hashlib.md5(s).hexdigest()
        print i, h
        if h[0:nb] == '0' * nb:
            print 'FOUND'
            break

        i += 1

if __name__ == '__main__':
    secret = 'yzbqklnj'
    mine(secret, 6)
