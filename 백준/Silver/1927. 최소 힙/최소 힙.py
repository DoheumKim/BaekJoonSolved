import heapq
import sys

# 빠른 입력을 위해 전체 데이터를 한 번에 읽음
data = sys.stdin.read().split()
if not data:exit()

n = int(data[0])
heap = []
ans = []

for i in range(1, n + 1):
    x = int(data[i])
    if x > 0:
        heapq.heappush(heap, x)
    else:
        # 힙이 비어있으면 0, 아니면 최솟값 추출
        if heap:ans.append(str(heapq.heappop(heap)))
        else:ans.append("0")

sys.stdout.write("\n".join(ans) + "\n")