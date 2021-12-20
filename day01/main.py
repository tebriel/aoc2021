#!/usr/bin/env python
import logging

logging.basicConfig(level=logging.INFO)

log = logging.getLogger(__name__)

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

    start = sum(int(line.strip()) for line in lines[0:3])
    log.debug("start: %s", start)
    increments = 0

    print(f"{lines[0].strip()} (N/A - no previous measurement)")
    for i in range(1, len(lines)-2):
        now = sum(int(line.strip()) for line in lines[i:i+3])
        log.debug("now: %s, i: %s", now, i)
        if now > start:
            increments += 1
            print(f"{lines[i].strip()} (increased)")
        elif now == start:
            print(f"{lines[i].strip()} (no change)")
        else:
            print(f"{lines[i].strip()} (decreased)")
        start = now

    return increments



print(count_increments('test.txt'))
print(count_increments('input.txt'))
print(count_window_increments('test.txt'))
print(count_window_increments('input.txt'))
