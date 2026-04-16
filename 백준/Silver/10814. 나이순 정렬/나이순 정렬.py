import sys

n = int(sys.stdin.readline())

members = []
for _ in range(n):
    age, name = sys.stdin.readline().split()
    members.append((int(age), name))

members.sort(key=lambda x: x[0])

for member in members:
    sys.stdout.write(str(member[0]) + " " + member[1] + "\n")