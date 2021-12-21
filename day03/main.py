"""Day 3"""

def process(filename) -> int:
    with open(filename) as infile:
        lines = infile.readlines()

    ones = [0 for _ in range(len(lines[0].strip()))]
    # Part 1
    for line in lines:
        line = line.strip()
        for idx, i in enumerate(line):
            if i == '1':
                ones[idx] += 1
    
    gamma_str = ''
    episolon_str = ''
    for one in ones:
        if one > (len(lines) / 2):
            gamma_str += '1'
            episolon_str += '0'
        else:
            gamma_str += '0'
            episolon_str += '1'

    gamma = int(f"0b{gamma_str}" , 2)
    epsilon= int(f"0b{episolon_str}" , 2)

    print(f"Gamma: {gamma}, Epsilon: {epsilon}")
    return gamma * epsilon


if __name__ == '__main__':
    print(process('test.txt'))
    print(process('input.txt'))
