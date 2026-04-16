import sys

n = int(sys.stdin.readline())
x, y = map(int, sys.stdin.readline().split())

if n == 1:print(0)
else:
    count = 0
    if x != 1: count += 1
    if x != n: count += 1
    if y != 1: count += 1
    if y != n: count += 1
    
    print(count)