import sys

input_data = sys.stdin.read().split()
N, M, B = map(int, input_data[:3])
land = list(map(int, input_data[3:]))

# 빈도수 배열을 사용하여 좌표 순회 횟수를 획기적으로 줄임 (500x500 -> 257)
height_counts = [0] * 257
for h in land:
    height_counts[h] += 1

min_time = float('inf')
best_height = 0

# 0부터 256까지 가능한 모든 높이 전수 조사
for target in range(257):
    removed = 0
    added = 0
    
    # 각 높이별 블록 개수를 기준으로 계산
    for current_h, count in enumerate(height_counts):
        if count == 0: continue
        
        if current_h > target:
            removed += (current_h - target) * count
        else:
            added += (target - current_h) * count
            
    # 인벤토리 잔여 블록 확인
    if removed + B >= added:
        time = removed * 2 + added
        # 최소 시간 갱신 (시간이 같으면 더 높은 높이 선택)
        if time <= min_time:
            min_time = time
            best_height = target

print(min_time, best_height)