import sys

# 입력을 한 번에 읽어 처리 속도 향상
input_data = sys.stdin.read().split()
if not input_data:
    exit()

N, K, Q = map(int, input_data[:3])
idx = 3

# 각 경계(i와 i+1 사이)를 지나는 사탕 수의 변화량 기록
# diff[i]는 i번 경계와 i-1번 경계의 흐름 차이
diff = [0] * (N + 1)

for i in range(1, N + 1):
    for _ in range(K):
        color = int(input_data[idx])
        idx += 1
        
        dist = (color - i + N) % N
        # 개별 거리 제약은 기본
        if dist > Q:
            print(0)
            exit()
            
        if i <= color:
            # i -> i+1 -> ... -> color 경로의 경계들에 흐름 추가
            # i번 경계부터 color-1번 경계까지 +1
            diff[i] += 1
            diff[color] -= 1
        else:
            # i -> ... -> N -> 1 -> ... -> color (원형 이동)
            # i번부터 N-1번까지 +1, 0번(N-1 사이)부터 color-1번까지 +1
            diff[i] += 1
            diff[N] -= 1
            diff[0] += 1
            diff[color] -= 1

# 경계별 상대적 흐름 계산
flows = [0] * N
current = 0
for i in range(N):
    current += diff[i]
    flows[i] = current

# 최댓값과 최솟값의 차이가 N 이하인지 확인하는 것이 핵심이 아니라,
# 모든 흐름 f_i를 f_i + m*N (m은 정수)으로 조절하여 0 <= f_i <= Q를 만족해야 함
# 이 문제에서 m은 0일 수밖에 없음 (사탕을 한 바퀴 더 돌릴 필요가 없으므로)

f_max = max(flows)
f_min = min(flows)

# 모든 경계의 흐름이 0 이상 Q 이하가 되도록 조정 가능한지 판단
# 0 <= flows[i] + offset <= Q 를 만족하는 정수 offset이 존재해야 함
# 즉, max(flows) - min(flows) 가 Q 이하인지만 보는 것이 아니라
# 흐름의 절댓값이 중요함. 이 로직에서는 f_max <= Q 이면 가능함.
if f_max <= Q:
    print(1)
else:
    print(0)