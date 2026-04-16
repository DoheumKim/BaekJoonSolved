import sys

n = int(sys.stdin.readline())
people = []

for _ in range(n):
    weight, height = map(int, sys.stdin.readline().split())
    people.append((weight, height))

for i in range(n):
    rank = 1
    for j in range(n):
        if i == j:continue
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:rank += 1    
    sys.stdout.write(str(rank) + " ")