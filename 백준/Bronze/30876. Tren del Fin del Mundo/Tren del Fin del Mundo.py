import sys

n = int(sys.stdin.readline())
stations = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
most_southern_station = min(stations, key=lambda x: x[1])

print(f"{most_southern_station[0]} {most_southern_station[1]}")