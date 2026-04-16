import sys

m, n = map(int, sys.stdin.readline().split())
# 0부터 n까지의 소수 여부를 저장하는 리스트 (초기값 True)
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False # 0과 1은 소수가 아님

# 에라토스테네스의 체 알고리즘
for i in range(2, int(n**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, n + 1, i):is_prime[j] = False

for i in range(m, n + 1):
    if is_prime[i]: sys.stdout.write(str(i) + "\n")