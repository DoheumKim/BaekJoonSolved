import sys

def solve():
    s = sys.stdin.readline().strip()
    if not s:
        print(0)
        return

    mod = 1000000009
    
    # 첫 번째 자리 초기화
    if s[0] == 'c':
        ans = 26
    else:
        ans = 10
        
    # 두 번째 자리부터 순회
    for i in range(1, len(s)):
        if s[i] == 'c':
            if s[i-1] == 'c': # 같은 종류 연속
                ans *= 25
            else: # 다른 종류
                ans *= 26
        else: # s[i] == 'd'
            if s[i-1] == 'd': # 같은 종류 연속
                ans *= 9
            else: # 다른 종류
                ans *= 10
        
        # 매번 나머지 연산 수행
        ans %= mod
        
    print(ans)

solve()