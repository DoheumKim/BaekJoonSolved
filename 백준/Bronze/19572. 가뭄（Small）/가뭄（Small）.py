import sys

d1, d2, d3 = map(int, sys.stdin.readline().split())

s = (d1 + d2 + d3) / 2
a = s - d3
b = s - d2
c = s - d1
if a > 0 and b > 0 and c > 0:
    print(1)
    print(f"{a:.1f} {b:.1f} {c:.1f}")
else:print(-1)