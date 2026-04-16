import sys

t = int(sys.stdin.readline())

for _ in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    floor0 = [i for i in range(1, n + 1)]
    for _ in range(k):
        new_floor = []
        for j in range(n):
            new_floor.append(sum(floor0[:j + 1]))
        floor0 = new_floor
    print(floor0[-1])

