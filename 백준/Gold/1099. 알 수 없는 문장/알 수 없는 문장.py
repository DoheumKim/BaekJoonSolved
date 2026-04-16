import sys

sentence = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for _ in range(n)]

L = len(sentence)
dp = [float('inf')] * (L + 1)
dp[0] = 0

def get_cost(s1, s2):
    if len(s1) != len(s2) or sorted(s1) != sorted(s2):return -1
    cost = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:cost += 1
    return cost
for i in range(1, L + 1):
    for j in range(i):
        sub = sentence[j:i]
        if dp[j] != float('inf'):
            for word in words:
                cost = get_cost(sub, word)
                if cost != -1:dp[i] = min(dp[i], dp[j] + cost)
if dp[L] == float('inf'):print(-1)
else:print(dp[L])