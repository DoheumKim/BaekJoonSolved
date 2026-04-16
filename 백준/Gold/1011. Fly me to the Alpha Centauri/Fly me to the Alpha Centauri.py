import sys
import math

t_input = sys.stdin.readline().strip()
if not t_input:exit()
T = int(t_input)

for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    distance = y - x
    n = int(math.sqrt(distance))
    
    if n ** 2 == distance:print(2 * n - 1)
    elif distance <= n ** 2 + n:print(2 * n)
    else:print(2 * n + 1)