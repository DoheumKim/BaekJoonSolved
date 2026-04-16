import sys
from collections import Counter

t = int(sys.stdin.readline())

for case_num in range(1, t + 1):
    n = int(sys.stdin.readline())
    prices = list(map(int, sys.stdin.readline().split()))

    counts = Counter(prices)
    sale_prices = []
    
    for p in prices:
        if counts[p] == 0:
            continue
        
        sale_prices.append(p)
        counts[p] -= 1 # 할인가 사용 처리
        
        normal_p = (p // 3) * 4
        counts[normal_p] -= 1 # 대응하는 정상가도 사용 처리
        
    print(f"Case #{case_num}: {' '.join(map(str, sale_prices))}")