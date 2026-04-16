import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    clothes = {}
    
    # 의상 종류별로 개수 세기
    for _ in range(n):
        _, category = sys.stdin.readline().split()
        clothes[category] = clothes.get(category, 0) + 1
    
    # 조합 계산
    ans = 1
    for count in clothes.values():
        ans *= (count + 1)
    print(ans - 1)