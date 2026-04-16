import sys

n = int(sys.stdin.readline())
# 인덱스 편의를 위해 0번 칸을 비우고 1번부터 점수 저장
s = [0] + [int(sys.stdin.readline()) for _ in range(n)]

# 계단이 2개 이하인 경우 예외 처리
if n == 1: print(s[1]); exit()
if n == 2: print(s[1] + s[2]); exit()

# DP 테이블 초기화
dp = [0] * (n + 1)
dp[1] = s[1]
dp[2] = s[1] + s[2]
dp[3] = max(s[1] + s[3], s[2] + s[3])

# 4번째 계단부터 점화식 적용
for i in range(4, n + 1):
    dp[i] = max(dp[i-2] + s[i], dp[i-3] + s[i-1] + s[i])

print(dp[n])