import sys

t = int(sys.stdin.readline())
for _ in range(t):
    steps = sys.stdin.readline().strip()
    fall_index = steps.find('D')
    print(len(steps) if fall_index == -1 else fall_index)