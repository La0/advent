from hashlib import md5

def crack(door_id):
    index = 0
    password = ''
    while len(password) < 8:
        contents = door_id + str(index)
        h = md5(contents).hexdigest()
        if h[:5] == '00000':
            print(index, contents, h)
            password += h[5]
        index += 1

    return password


if __name__ == '__main__':
    print(crack('abbhdwsy'))
