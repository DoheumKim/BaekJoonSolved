import sys

t = int(sys.stdin.readline())

for _ in range(t):
    # H: 층 수, W: 방 수, N: N번째 손님
    h, w, n = map(int, sys.stdin.readline().split())
    floor = n % h
    room_num = (n // h) + 1
    
    # n이 h의 배수일 때 (꼭대기 층인 경우) 예외 처리
    if floor == 0:
        floor = h
        room_num -= 1
        
    # 층수 * 100 + 호수
    print(floor * 100 + room_num)