import sys

# 빠른 입력 처리
input_data = sys.stdin.read().split()
if not input_data:
    exit()

N, K, Q = map(int, input_data[:3])
idx = 3

# 각 위치(i)에서 목표 위치(c)로 가야 하는 사탕의 분포를 기록
# count[i] = (i번 위치에 있는 사탕들이 이동해야 할 총 거리의 지표)
# 실제로는 구간 합을 이용하기 위해 'i번 위치에서 나가야 하는 사탕의 순수 변화량'을 계산함
diff = [0] * (N + 1)

for i in range(1, N + 1):
    # i번 깡통에서 나가는 사탕들은 기본적으로 i번 깡통이 목표가 아닌 것들임
    # 하지만 더 정확하게는 '누적 흐름'의 관점에서 접근해야 함
    for _ in range(K):
        color = int(input_data[idx])
        idx += 1
        # dist: 시계 방향으로 이동해야 할 거리
        dist = (color - i + N) % N
        
        # 개별 사탕의 거리가 Q를 넘으면 즉시 실패 (서브태스크 3 해결)
        if dist > Q:
            print(0)
            exit()
            
        # 1번 깡통을 지나는 흐름을 계산하기 위한 처리
        if i > color:
            diff[0] += 1 # 1번 깡통을 통과함
        diff[color] -= 1
        diff[i] += 1

# 깡통 사이의 흐름(Flow) 계산
current_flow = diff[0]
max_flow = current_flow

for i in range(1, N):
    current_flow += diff[i]
    if current_flow > max_flow:
        max_flow = current_flow

# 전체 구간 중 가장 많이 흐르는 사탕의 수가 Q를 초과하는지 확인
if max_flow <= Q:
    print(1)
else:
    print(0)