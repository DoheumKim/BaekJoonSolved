'''문제
원기둥 형태의 뚜껑이 없는 깡통 N개가 원형으로 배열되어 있다. 각 깡통에는 시계 방향 순서대로 1번부터 N번까지의 자연수 번호가 붙어 있으며, 각 깡통에는 사탕이 K개씩 들어 있다. 따라서, 총 N ×K개의 사탕이 있는 것이다.

모든 사탕은 1 이상 N 이하의 자연수로 표현되는 색깔을 가진다. 모든 색 c (1 ≤ c ≤ N)에 대해, 깡통에 들어 있는 총 N × K개의 사탕 중 색깔이 c인 사탕은 정확히 K개 있다. 각 깡통에 들어 있는 사탕의 색이 무엇인지는 입력으로 주어진다.

이때 사탕 돌리기라는 연산은 아래와 같이 사탕을 하나씩 옮기는 N개의 작업을, 아래에 주어진 순서대로 수행하는 것을 말한다.

1번 깡통에서 임의로 사탕을 하나 꺼내 2번 깡통에 넣는다.
2번 깡통에서 임의로 사탕을 하나 꺼내 3번 깡통에 넣는다.
3번 깡통에서 임의로 사탕을 하나 꺼내 4번 깡통에 넣는다.
.......
(N − 1)번 깡통에서 임의로 사탕을 하나 꺼내 N번 깡통에 넣는다.
N번 깡통에서 임의로 사탕을 하나 꺼내 1번 깡통에 넣는다.
당신은 주어진 초기 상태에서 사탕 돌리기를 정확히 Q번 반복 수행할 것이다. 수행한 이후에 당신은 c의 색깔을 가지는 모든 사탕이 c번 깡통에 들어가도록 하고 싶다. 즉, 1번 깡통에는 1번 색깔의 사탕만이 존재하고, 2번 깡통에는 2번 색깔의 사탕만이 존재하고, ...., 마지막으로 N번 깡통에는 N번 색깔의 사탕만이 존재하도록 하고자 한다. 이러한 상태를 올바른 상태라고 하자.

입력으로 각 깡통에 들어 있는 사탕의 상황이 주어질 때, 초기 상태에서 사탕 돌리기를 정확히 Q번 반복 수행한 후 위에서 설명한 올바른 상태를 이룰 수 있는지 판단하는 프로그램을 작성하라.

입력
첫 번째 줄에 N, K, Q가 공백 하나를 사이로 두고 주어진다.

이어지는 N개의 줄의 각 i (1 ≤ i ≤ N)번째 줄에는 1 이상 N 이하인 K개의 정수가 공백 하나씩을 사이로 두고 주어지며, 이는 초기 상태에서 i번 깡통에 들어 있는 K개의 사탕의 색깔들을 의미한다.

출력
입력으로 주어진 초기 상태에서 사탕 돌리기를 정확히 Q번 반복 수행하여 올바른 상태로 만들 수 있다면 숫자 1을, 아니면 숫자 0을 출력한다.

제한
2 ≤ N ≤ 2 000
1 ≤ K ≤ 2 000
1 ≤ Q ≤ 1 000 000 000
모든 색깔 c (1 ≤ c ≤ N)에 대해, 색깔이 c인 사탕은 정확히 K개 있다.
서브태스크
번호	배점	제한
1	3	
Q = 1

2	6	
N = 2

3	28	
K = 1

4	40	
N, K ≤ 100

5	23	
추가 제약 조건 없음

예제 입력 1 
3 1 1
2
3
1
예제 출력 1 
1'''
import sys

input = sys.stdin.readline
N, K, Q = map(int, input().split())
arr = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    colors = map(int, input().split())
    for color in colors:
        arr[i][color] += 1

# delta[i][c]: i번 깡통의 c색 사탕의 (초기 개수 - 목표 개수)
delta = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for c in range(1, N + 1):
        # 목표: i번 깡통에는 i색 사탕만 K개 있어야 함
        goal = K if i == c else 0
        delta[i][c] = arr[i][c] - goal

# out_prefix_sum[i][c]: 1번부터 i번 깡통까지의 델타 누적합
out_prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]
# 1번 깡통의 누적합은 델타값과 동일
for c in range(1, N + 1):out_prefix_sum[1][c] = delta[1][c]
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
        # Out[1][c]는 모든 -S[i][c]보다 크거나 같아야 함.
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
