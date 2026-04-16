import sys

n = int(sys.stdin.readline())
total_remains = 0

for _ in range(n):
    students, apples = map(int, sys.stdin.readline().split())
    total_remains += apples % students

print(total_remains)