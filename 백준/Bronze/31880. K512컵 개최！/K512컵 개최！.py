import sys

n, m = map(int, sys.stdin.readline().split())
adds = list(map(int, sys.stdin.readline().split()))
muls = list(map(int, sys.stdin.readline().split()))

# 모든 덧셈을 먼저 수행 (초기 행운 수치 0에서 시작)
current_luck = sum(adds)

# 1보다 큰 곱셈 주문서만 골라서 곱함
# (0은 초기에 써서 0인 상태를 유지하고, 1은 곱해도 그대로이므로)
for b in muls:
    if b > 1:
        current_luck *= b

print(current_luck)