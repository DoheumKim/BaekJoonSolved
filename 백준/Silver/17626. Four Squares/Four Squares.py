import sys

def solve():
    n = int(sys.stdin.readline())
    # 1. 결과가 1인 경우 (n 자체가 제곱수)
    if int(n**0.5)**2 == n:return 1
    
    # 제곱수 리스트 미리 생성
    squares = [i*i for i in range(1, int(n**0.5) + 1)]
    
    # 2. 결과가 2인 경우 (n - i*i 가 제곱수)
    for s in squares:
        if int((n - s)**0.5)**2 == (n - s):return 2
        
    # 3. 결과가 3인 경우 (n - i*i - j*j 가 제곱수)
    for s1 in squares:
        for s2 in squares:
            if s1 + s2 >= n: break
            if int((n - s1 - s2)**0.5)**2 == (n - s1 - s2):return 3
    return 4

print(solve())