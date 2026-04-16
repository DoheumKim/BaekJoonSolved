import sys

dp = [0] * 101
dp[1], dp[2], dp[3] = 1, 1, 1
dp[4], dp[5] = 2, 2

for i in range(6, 101):dp[i] = dp[i-2] + dp[i-3]

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(dp[n])