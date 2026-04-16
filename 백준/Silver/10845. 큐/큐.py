import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    cmd = sys.stdin.readline().split()
    op = cmd[0]

    if op == "push": queue.append(int(cmd[1]))
    elif op == "pop": print(queue.popleft() if queue else -1)
    elif op == "size": print(len(queue))
    elif op == "empty": print(1 if not queue else 0)
    elif op == "front": print(queue[0] if queue else -1)
    elif op == "back": print(queue[-1] if queue else -1)