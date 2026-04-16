import sys

# N: 저장된 사이트 수, M: 찾으려는 사이트 수
n, m = map(int, sys.stdin.readline().split())

# 사이트 주소를 Key로, 비밀번호를 Value로 저장
passwords = {}
for _ in range(n):
    site, pw = sys.stdin.readline().split()
    passwords[site] = pw

# M개의 사이트에 대해 비밀번호 즉시 조회 및 출력
for _ in range(m):
    target_site = sys.stdin.readline().strip()
    sys.stdout.write(passwords[target_site] + "\n")