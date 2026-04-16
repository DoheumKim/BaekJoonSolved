import sys

# K: 가진 랜선 수, N: 필요한 랜선 수
k, n = map(int, sys.stdin.readline().split())
lines = [int(sys.stdin.readline()) for _ in range(k)]

# 이분 탐색 범위 설정
start, end = 1, max(lines)
result = 0

while start <= end:
    mid = (start + end) // 2
    
    # mid 길이로 잘랐을 때 나오는 총 랜선 수 계산
    total_count = 0
    for line in lines:total_count += line // mid
    
    # 필요한 개수 N을 충족하는지 확인
    if total_count >= n:
        # 일단 N개 이상 만들었으므로 현재 길이를 저장하고, 더 긴 길이를 탐색
        result = mid
        start = mid + 1
    else:end = mid - 1

print(result)