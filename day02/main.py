"""Day 02"""
from strenum import StrEnum
from dataclasses import dataclass

class Direction(StrEnum):
    FORWARD = 'forward'
    DOWN = 'down'
    UP = 'up'

@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=True)
class Command:
    direction: Direction
    distance: int


def run(filename) -> int:
    instructions = []
    with open(filename) as test:
        for line in test.readlines():
            line = line.strip().split()
            instructions.append(Command(Direction(line[0]), int(line[1])))

    horizontal = 0
    depth = 0
    aim = 0
    for instruction in instructions:
        if instruction.direction == Direction.FORWARD:
            horizontal += instruction.distance
            depth += aim * instruction.distance
        elif instruction.direction == Direction.DOWN:
            aim += instruction.distance
        elif instruction.direction == Direction.UP:
            aim -= instruction.distance

    return horizontal * depth


if __name__ == '__main__':
    print(run('test.txt'))
    print(run('input.txt'))
