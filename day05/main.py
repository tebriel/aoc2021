"""Day 05"""
def process(filename):
    segments = []
    max_x = 0
    max_y = 0
    with open(filename) as infile:
        for line in infile.readlines():
            start, end = line.strip().split(' -> ')
            start = [int(x) for x in start.split(',')]
            end = [int(x) for x in end.split(',')]
            segments.append((start, end,))
            max_x = max(max_x, max(start[0], end[0]))
            max_y = max(max_y, max(start[1], end[1]))

    graph = []
    for _ in range(max_y + 1):
        graph.append([0]*(max_x+1))

    for segment in segments:
        start, end = segment
        
        # if start[0] != end[0] and start[1] != end[1]:
        #     continue
        # start, end = order_segments(start, end)
        # start, end = expand_range(start, end)
        # print(start, end)
        cur_x, cur_y = start
        # print(cur_x, cur_y)
        graph[cur_y][cur_x] += 1
        while (cur_x != end[0] or cur_y != end[1]):
            if cur_x < end[0]:
                cur_x += 1
            elif cur_x > end[0]:
                cur_x -= 1
            if cur_y < end[1]:
                cur_y += 1
            elif cur_y > end[1]:
                cur_y -= 1
            # print(cur_x, cur_y)
            graph[cur_y][cur_x] += 1


        # for x in range(start[0], end[0], direction_x):
        #     for y in range(start[1], end[1], direction_y):
        #         print(f"{x}, {y}")
        #         graph[y][x] += 1

    dangerous_count = 0
    for row in graph:
        for x in row:
            if x >= 2:
                dangerous_count += 1
        print(''.join(['.' if x == 0 else str(x) for x in row]))
    print(f"Dangerous count: {dangerous_count}")

def expand_range(o_start, o_end):
    start = o_start.copy()
    end = o_end.copy()
    for x in range(2):
        if start[x] <= end[x]:
            end[x] = end[x] + 1
        elif end[x] < start[x]:
            end[x] = end[x] - 1
    return start, end

def order_segments(start, end):
    if start[0] == end[0]:
        if start[1] < end[1]:
            return start, end
        else:
            return end, start
    elif start[1] == end[1]:
        if start[0] < end[0]:
            return start, end
        else:
            return end, start
    else:
        raise Exception('Invalid segment')

if __name__ == '__main__':
    process('test.txt')
    process('input.txt')
