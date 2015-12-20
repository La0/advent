def house(x):
    return sum([i for i in range(1, x+1) if x % i == 0])


def find_house(target):
    target /= 10
    houses = [1, ] * target

    for elf in range(2, target):
        for house in range(elf-1, target, elf):
            #print 'Add %d to house %d' % (elf, house+1)
            houses[house] += elf

    return min([i for i,h in enumerate(houses) if h >= target]) + 1

    return houses.index(target) + 1


if __name__ == '__main__':
    print find_house(150)
    print find_house(36000000)
