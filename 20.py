def house(x):
    return sum([i for i in range(1, x+1) if x % i == 0])


def find_house(target):
    nb = 11
    houses = [nb, ] * target

    for elf in range(2, target / 10):
        nb_houses = 0
        for house in range(elf-1, target / 10, elf):
            #print 'Add %d to house %d' % (elf, house+1)
            houses[house] += elf * nb
            nb_houses += 1

            if nb_houses >= 50:
                break

    return min([i for i,h in enumerate(houses) if h >= target]) + 1


if __name__ == '__main__':
    print find_house(150)
    print find_house(36000000)
