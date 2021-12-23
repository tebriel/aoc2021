"""Day 06"""

def process(filename):
    fishes = {x: 0 for x in range(9)}

    with open(filename) as infile:
        for fish in infile.readline().strip().split(','):
            fishes[int(fish)] += 1
    
    for day in range(80):
        new_fishes = {x: 0 for x in range(9)}
        for age, count in fishes.items():
            if count == 0:
                continue
            if age == 0:
                new_fishes[6] = count
                new_fishes[8] = count
            else:
                new_fishes[age - 1] += count
        fishes = new_fishes
        # print(fishes)

        if day == 17:
            print(f"Day 17: {sum(fishes.values())}")

    print(f"Day 80: {sum(fishes.values())}")

if __name__ == '__main__':
    process('test.txt')
    process('input.txt')
