def find_code(row, col):

    # Find nb of iterations
    side = row + col - 1
    area = sum(xrange(side))
    area += col

    code = 20151125
    for i in range(area - 1):
        code = (code * 252533) % 33554393

    return code

if __name__ == '__main__':
    print find_code(5,2) == 17552253
    print find_code(2981, 3075)
