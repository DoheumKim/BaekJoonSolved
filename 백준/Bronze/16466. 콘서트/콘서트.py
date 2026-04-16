import sys

n = int(sys.stdin.readline());idx = 1
nums = set(map(int, sys.stdin.readline().split()))
# set써서 탐색 속도를 O(1)로 최적화
while idx in nums: idx += 1
print(idx)