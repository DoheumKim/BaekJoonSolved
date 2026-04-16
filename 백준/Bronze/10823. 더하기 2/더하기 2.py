import sys

data = sys.stdin.read().replace('\n', '')
nums = [int(x) for x in data.split(',') if x]

print(sum(nums))