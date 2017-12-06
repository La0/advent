def realloc(banks):
    assert isinstance(banks, list)
    configurations = []

    while banks not in configurations:
        # Save previous configuration
        configurations.append(list(banks))

        # Find max and its first pos
        block = max(banks)
        pos = banks.index(block)

        # Reset bank
        banks[pos] = 0

        # Distribute on banks
        for i in range(1, block+1):
            banks[(pos + i)%len(banks)] += 1

    length = len(configurations)
    return (
        length,
        length - configurations.index(banks)
    )

if __name__ == '__main__':
    assert realloc([0, 2, 7, 0]) == (5, 4)

    with open('6.txt') as f:
        banks = list(map(int, f.read().split(' ')))
        print(realloc(banks))
