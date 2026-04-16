import sys

s = sys.stdin.readline().strip()
n = int(s)

# (7 포함 여부 * 2) + (7로 나누어떨어짐 * 1)
result = ('7' in s) * 2 + (n % 7 == 0) * 1
print(result)