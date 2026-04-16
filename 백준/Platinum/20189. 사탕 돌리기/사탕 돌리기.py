import sys

def solve():
    # 메모리 절약을 위해 입력을 하나씩 산출하는 제너레이터 사용
    def get_ints():
        for line in sys.stdin:
            for token in line.split():
                yield int(token)
    
    tokens = get_ints()
    try:
        N = next(tokens)
        K = next(tokens)
        Q = next(tokens)
    except StopIteration:
        return

    # diff: 각 경계선(Edge)을 지나는 사탕의 총 개수 계산용 (기존 9점 코드의 핵심)
    diff = [0] * (N + 1)
    
    # grid[S][E']: 출발지 S에서 목적지 E'로 가는 사탕들이 소비하는 "총 거리(시간)"
    grid = [[0] * (N + 1) for _ in range(N)]

    for i in range(1, N + 1):
        S = i - 1  # 0-indexed 변환
        for _ in range(K):
            color = next(tokens)
            C = color - 1
            
            d = (C - S + N) % N
            if d == 0:
                continue
                
            # E_prime: 목적지를 1~N으로 매핑 (C=0일 때 N으로 처리하여 시간축 계산 편의성 확보)
            E_prime = C if C > 0 else N
            grid[S][E_prime] += d
            
            # 구간 누적합을 위한 설정
            if S + d <= N:
                diff[S] += 1
                diff[S + d] -= 1
            else:
                diff[S] += 1
                diff[N] -= 1
                diff[0] += 1
                diff[(S + d) % N] -= 1

    # 조건 1: 단일 경계선을 지나는 총 사탕의 개수가 Q를 초과하면 실패
    current_flow = 0
    for i in range(N):
        current_flow += diff[i]
        if current_flow > Q:
            print(0)
            return
            
    # 조건 2: 타이밍 병목 검사 (스케줄링 데드라인 한계 체크)
    # sum_S[A][B] = 목적지가 B이고, 출발지가 A 이상인 사탕들의 거리 총합
    sum_S = [[0] * (N + 1) for _ in range(N + 1)]
    for B in range(1, N + 1):
        s = 0
        for A in range(N - 1, -1, -1):
            s += grid[A][B]
            sum_S[A][B] = s
            
    # A(출발점 하한)와 B(도착점 상한)를 기준으로 요구되는 시간이 가능한 시간 용량을 넘는지 전수조사
    for A in range(N):
        current_sum = 0
        for B in range(1, N + 1):
            current_sum += sum_S[A][B]
            
            # 해당 구간에서 사탕들이 스케줄링 될 수 있는 최대 허용 시간(Capacity)
            capacity = Q * N - N + B - A
            
            # 요구되는 총 이동 거리(current_sum)가 허용 시간을 초과하면 실패
            if current_sum > 0 and current_sum > capacity:
                print(0)
                return
                
    # 모든 병목 조건을 통과하면 성공
    print(1)

if __name__ == '__main__':
    solve()