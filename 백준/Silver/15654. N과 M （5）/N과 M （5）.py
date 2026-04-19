import sys
from itertools import permutations

input_data = sys.stdin.read().split()
N, M = map(int, input_data[:2])
nums = sorted(map(int, input_data[2:]))

# permutations는 정렬된 입력에 대해 사전 순으로 순열을 생성함
for p in permutations(nums, M):print(*(p))