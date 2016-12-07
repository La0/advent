from hashlib import md5

def crack(door_id):
    index = 0
    password = [' '] * 8
    while ' ' in password:
        contents = door_id + str(index)
        h = md5(contents).hexdigest()
        if h[:5] == '00000':
            print(index, contents, h)
            try:
                pos = int(h[5])
                if password[pos] != ' ':
                    raise Exception('already filled {}'.format(pos))
                password[pos] = h[6]
            except Exception as e:
                print('error', e)
        index += 1

    return ''.join(password)


if __name__ == '__main__':
    print(crack('abbhdwsy'))
