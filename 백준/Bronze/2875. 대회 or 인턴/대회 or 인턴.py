import sys

n, m, k = map(int, sys.stdin.readline().split())

teams = 0
# 팀을 하나씩 늘려가며 조건(여 2명 이상, 남 1명 이상, 남은 인원이 k명 이상) 확인
while n >= 2 and m >= 1 and (n + m - 3) >= k:
    n -= 2
    m -= 1
    teams += 1

print(teams)