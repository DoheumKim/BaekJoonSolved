import sys

round_fn = lambda val: int(val + 0.5)
n = int(sys.stdin.readline())

if n == 0:print(0)
else:
    opinions = sorted([int(sys.stdin.readline()) for _ in range(n)])
    trim = round_fn(n * 0.15)
    target = opinions[trim : n - trim]
    print(round_fn(sum(target) / len(target)))