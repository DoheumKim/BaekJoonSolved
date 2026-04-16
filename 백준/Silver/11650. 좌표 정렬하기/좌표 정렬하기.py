import sys

n = int(sys.stdin.readline())
points = []

for _ in range(n):points.append(list(map(int, sys.stdin.readline().split())))

points.sort()

for point in points:sys.stdout.write(str(point[0]) + " " + str(point[1]) + "\n")