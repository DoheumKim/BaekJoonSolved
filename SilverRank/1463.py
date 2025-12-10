# 그리디 알고리즘(Greedy Algorithm) 방식
import sys
X = int(sys.stdin.readline())
trial = 0
while True:
    # print(X)
    if (X - 1) % 3 == 0:
        X -= 1
        # print(X)
        X //= 3
        trial += 1
    elif X % 3 == 0:X //= 3
    elif (X - 1) % 2 == 0:
        X -= 1
        # print(X)
        X //= 2
        trial += 1
    elif X % 2 == 0:X //= 2
    else:X -= 1
    trial += 1
    if X == 1: break
print(trial)