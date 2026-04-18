import sys
from itertools import combinations_with_replacement

input_data = sys.stdin.read().split()
N, M = map(int, input_data)

nums = range(1, N + 1)

for combo in combinations_with_replacement(nums, M):print(*(combo))