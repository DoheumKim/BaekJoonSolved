import sys

input = sys.stdin.readline
N, K, Q = map(int, input().split())
initial_state = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    colors = map(int, input().split())
    for color in colors:
        initial_state[i][color] += 1

delta = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for c in range(1, N + 1):
        goal = K if i == c else 0
        delta[i][c] = initial_state[i][c] - goal

out_prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]

for c in range(1, N + 1):out_prefix_sum[1][c] = delta[1][c]

for i in range(2, N + 1):
    for c in range(1, N + 1):
        out_prefix_sum[i][c] = out_prefix_sum[i - 1][c] + delta[i][c]

min_needed_from_can_1 = [0] * (N + 1)
for c in range(1, N + 1):
    max_negative_sum = 0
    for i in range(1, N + 1):
        if -out_prefix_sum[i][c] > max_negative_sum:
            max_negative_sum = -out_prefix_sum[i][c]
    min_needed_from_can_1[c] = max_negative_sum

total_min_needed = sum(min_needed_from_can_1)

if total_min_needed <= Q:print(1)
else:print(0)