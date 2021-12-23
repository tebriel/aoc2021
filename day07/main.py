"""Day 07"""

def process(filename):
    with open(filename) as infile:
        positions = [int(x) for x in infile.readline().strip().split(',')]

    min_x = min(positions)
    max_x = max(positions)
    costs = {x: 0 for x in range(min_x, max_x + 1)}

    for pos in costs.keys():
        for crab in positions:
            distance = abs(pos - crab)
            costs[pos] += ((distance * distance) + distance) // 2

    print(f"Day 07: {min(costs.values())}")

if __name__ == '__main__':
    process('test.txt')
    process('input.txt')
