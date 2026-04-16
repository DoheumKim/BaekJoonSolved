import sys
x, y, w, h = map(int,(sys.stdin.readline().split()))
res = min(x, y, w - x, h - y)

print(res)