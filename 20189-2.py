import sys

# 입력을 빠르게 받기 위한 설정
input = sys.stdin.readline

# N, K, Q 입력 받기
N, K, Q = map(int, input().split())

# 1번부터 N번 인덱스를 사용하기 위해 (N+1) x (N+1) 크기로 배열 선언
# initial_state[i][c]: i번 깡통의 c색 사탕 개수
initial_state = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    colors = map(int, input().split())
    for color in colors:
        initial_state[i][color] += 1

# delta[i][c]: i번 깡통의 c색 사탕의 (초기 개수 - 목표 개수)
delta = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for c in range(1, N + 1):
        # 목표: i번 깡통에는 i색 사탕만 K개 있어야 함
        goal = K if i == c else 0
        delta[i][c] = initial_state[i][c] - goal

# out_prefix_sum[i][c]: 1번부터 i번 깡통까지 델타의 누적합
out_prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]
# 1번 깡통의 누적합은 델타값과 동일
for c in range(1, N + 1):
    out_prefix_sum[1][c] = delta[1][c]
# 2번부터 N번 깡통까지 순회하며 누적합 계산
for i in range(2, N + 1):
    for c in range(1, N + 1):
        out_prefix_sum[i][c] = out_prefix_sum[i - 1][c] + delta[i][c]

# min_needed_from_can_1[c]: 1번 깡통에서 최소한 내보내야 하는 c색 사탕의 수
min_needed_from_can_1 = [0] * (N + 1)
for c in range(1, N + 1):
    max_negative_sum = 0
    for i in range(1, N + 1):
        # Out[i][c] = Out[1][c] + S[i][c] >= 0 이어야 하므로,
        # Out[1][c] >= -S[i][c] 여야 함.
        # 이 조건이 모든 i에 대해 만족해야 하므로,
        # Out[1][c]는 모든 -S[i][c] 값들보다 크거나 같아야 함.
        if -out_prefix_sum[i][c] > max_negative_sum:
            max_negative_sum = -out_prefix_sum[i][c]
    min_needed_from_can_1[c] = max_negative_sum

# 1번 깡통에서 내보내야 할 최소 사탕들의 총합
total_min_needed = sum(min_needed_from_can_1)

# 이 총합이 Q보다 작거나 같으면 목표 상태를 만들 수 있음
if total_min_needed <= Q:
    print(1)
else:
    print(0)