import sys

T = int(sys.stdin.readline())
coins = [25, 10, 5, 1]

for _ in range(T):
    money = int(sys.stdin.readline())
    result = []
    
    for coin in coins:
        result.append(money // coin)
        money %= coin
    
    print(*(result))