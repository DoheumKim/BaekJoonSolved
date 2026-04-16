import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    cmd = sys.stdin.readline().split()
    op = cmd[0]

    if op == "push": stack.append(int(cmd[1]))
    elif op == "pop": print(stack.pop() if stack else -1)
    elif op == "size": print(len(stack))
    elif op == "empty": print(1 if not stack else 0)
    elif op == "top": print(stack[-1] if stack else -1)