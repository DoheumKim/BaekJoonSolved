import sys

n = int(sys.stdin.readline())

# f(1) = 1, f(2) = 2
dp = [0] * (n + 1)

if n >= 1:dp[1] = 1
if n >= 2:dp[2] = 2

# f(i) = f(i-1) + f(i-2)
for i in range(3, n + 1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])