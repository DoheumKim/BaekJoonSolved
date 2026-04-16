import sys

n = int(sys.stdin.readline())
times = sorted(list(map(int, sys.stdin.readline().split())))

total_wait_time = 0
accumulated_time = 0

for time in times:
    accumulated_time += time # 현재 사람이 인출을 완료할 때까지 걸린 시간
    total_wait_time += accumulated_time # 모든 사람의 대기 시간 총합에 추가

print(total_wait_time)