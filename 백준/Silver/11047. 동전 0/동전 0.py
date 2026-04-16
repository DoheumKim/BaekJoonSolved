import sys

N, K = map(int, sys.stdin.readline().split())

coins = []
for _ in range(N):coins.append(int(sys.stdin.readline()))

count = 0

for i in range(N - 1, -1, -1):
    if K == 0:break

    count += K // coins[i]
    K %= coins[i]

print(count)