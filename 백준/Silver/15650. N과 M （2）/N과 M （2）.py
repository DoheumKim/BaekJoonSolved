import sys
from itertools import combinations

input_data = sys.stdin.read().split()

N, M = map(int, input_data)
nums = range(1, N + 1)
for combo in combinations(nums, M):print(*(combo))