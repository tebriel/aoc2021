#!/usr/bin/env python

def count_increments(filename: str) -> int:
    with open(filename) as test:
        lines = test.readlines()

    start = None
    increments = 0

    for line in lines:
        line = int(line.strip())
        if start is None:
            start = line
            continue
        if line > start:
            increments += 1
        start = line

    return increments

def count_window_increments(filename: str) -> int:
    with open(filename) as test:
        lines = test.readlines()

    start =

print(count_increments('test.txt'))
print(count_increments('input.txt'))