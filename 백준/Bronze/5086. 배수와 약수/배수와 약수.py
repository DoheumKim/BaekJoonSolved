import sys

while True:
    line = sys.stdin.readline().split()
    if not line:break
    a, b = map(int, line)
    if a == 0 and b == 0:break
    if b % a == 0:print("factor")
    elif a % b == 0:print("multiple")
    else:print("neither")