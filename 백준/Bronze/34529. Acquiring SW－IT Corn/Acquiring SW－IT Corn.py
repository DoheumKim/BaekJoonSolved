import sys

x, y, z = map(int, sys.stdin.readline().split())
u, v, w = map(int, sys.stdin.readline().split())
total_price = (u // 100 * x) + (v // 50 * y) + (w // 20 * z)

print(total_price)