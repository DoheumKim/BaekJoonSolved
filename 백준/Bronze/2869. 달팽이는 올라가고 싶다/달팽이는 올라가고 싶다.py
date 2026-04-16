import sys
import math

a, b, v = map(int, sys.stdin.readline().split())
days = math.ceil((v - b) / (a - b))
print(days)