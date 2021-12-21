"""Day 3"""
from typing import List, Tuple

def process(filename) -> int:
    with open(filename) as infile:
        lines = infile.readlines()

    gamma_str, episolon_str = find_count(lines)

    gamma = int(f"0b{gamma_str}" , 2)
    epsilon = int(f"0b{episolon_str}" , 2)

    ox_rating = int(f"0b{find_prefix(lines, True)}", 2)
    c02_rating = int(f"0b{find_prefix(lines, False)}", 2)

    print(f"Gamma: {gamma}, Epsilon: {epsilon}")
    print(f"Ox Rating: {ox_rating}, C02 Rating: {c02_rating}, Combined: {ox_rating * c02_rating}")
    return gamma * epsilon

def find_count(lines: List[str]) -> Tuple[str, str]:
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
        if one >= (len(lines) / 2):
            gamma_str += '1'
            episolon_str += '0'
        else:
            gamma_str += '0'
            episolon_str += '1'
    
    return gamma_str, episolon_str

def find_prefix(lines: List[str], use_g: bool) -> str:
    ox_lines = list(lines)
    for idx in range(len(ox_lines[0].strip())):
        if use_g:
            g, _ = find_count(ox_lines)
        else:
            _, g = find_count(ox_lines)
        ox_copy = list(ox_lines)
        for ox in ox_lines:
            if ox[idx] != g[idx]:
                ox_copy.remove(ox)
        if len(ox_copy) <= 1:
            break
        ox_lines = ox_copy
    if len(ox_copy) != 1:
        raise Exception("Could not find prefix")
    return ox_copy[0].strip()


if __name__ == '__main__':
    print(process('test.txt'))
    print(process('input.txt'))
