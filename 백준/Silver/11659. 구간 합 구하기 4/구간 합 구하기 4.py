import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
prefix_sum = [0] * (n + 1)
temp = 0

for i in range(n):
    temp += numbers[i]
    prefix_sum[i+1] = temp

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(prefix_sum[j] - prefix_sum[i-1])