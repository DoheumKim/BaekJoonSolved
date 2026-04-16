import sys

n, m = map(int, sys.stdin.readline().split())

unheard = set()
for _ in range(n):
    unheard.add(sys.stdin.readline().strip())

unseen = set()
for _ in range(m):
    unseen.add(sys.stdin.readline().strip())

result = sorted(list(unheard & unseen))

sys.stdout.write(str(len(result)) + '\n')
for name in result:
    sys.stdout.write(name + '\n')