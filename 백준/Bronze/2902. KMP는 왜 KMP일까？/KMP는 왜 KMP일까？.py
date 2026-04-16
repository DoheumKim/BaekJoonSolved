import sys

names = sys.stdin.readline().strip().split('-')
res = "".join(name[0] for name in names)
print(res)