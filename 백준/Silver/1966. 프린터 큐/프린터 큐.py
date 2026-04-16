import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    priorities = list(map(int, sys.stdin.readline().split()))
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    
    print_count = 0
    
    while queue:
        current_p = queue[0][0]
        if any(current_p < doc[0] for doc in queue):
            queue.append(queue.popleft())
        else:
            printed_doc = queue.popleft()
            print_count += 1
            if printed_doc[1] == m:
                print(print_count)
                break