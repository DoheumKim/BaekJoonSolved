import sys

while True:
    total, away = map(int, sys.stdin.readline().split())
    
    # 종료 조건
    if total == 0 and away == 0:
        break
        
    # 침실에 있는 인형 수
    in_room = total - away
    
    # 인형이 아예 없거나 1개뿐인 경우 (쌍이나 3명 그룹 불가)
    if in_room < 2:
        if in_room == 0:
            print(0, 0)
        else: # 1개일 때 (문제 조건상 2개씩 짝짓거나 3명 그룹이므로 1개는 남음)
            print(0, 0)
        continue

    # 짝수일 때
    if in_room % 2 == 0:
        print(in_room // 2, 0)
    # 홀수일 때 (3개 그룹 1개 생성)
    else:
        # 3개를 먼저 그룹화하고 남은 인원을 2로 나눔
        pairs = (in_room - 3) // 2
        print(max(0, pairs), 1)