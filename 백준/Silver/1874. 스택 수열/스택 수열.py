import sys

n = int(sys.stdin.readline())
stack = []
results = []
current_num = 1
is_possible = True

for _ in range(n):
    target = int(sys.stdin.readline())
    
    while current_num <= target:
        stack.append(current_num)
        results.append("+")
        current_num += 1
    
    if stack[-1] == target:
        stack.pop()
        results.append("-")
    else:
        is_possible = False
        break

if is_possible:
    sys.stdout.write("\n".join(results) + "\n")
else:
    print("NO")