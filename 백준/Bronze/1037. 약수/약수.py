import sys
count = int(sys.stdin.readline())
divisors = list(map(int, sys.stdin.readline().split()))
min_val = min(divisors)
max_val = max(divisors)
print(min_val * max_val)