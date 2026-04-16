import sys

def rev(n):
    return int(str(n)[::-1])

line = sys.stdin.readline().split()
if line:
    x, y = map(int, line)
    result = rev(rev(x) + rev(y))
    print(result)