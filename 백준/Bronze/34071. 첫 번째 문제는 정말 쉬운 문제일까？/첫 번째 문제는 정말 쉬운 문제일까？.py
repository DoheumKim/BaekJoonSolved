import sys

input_data = sys.stdin.readline
N = int(input_data())

arr = []
for _ in range(N):arr.append(int(input_data()))

first_val = arr[0]
max_val = max(arr)
min_val = min(arr)


if first_val == min_val:print("ez")
elif first_val == max_val:print("hard")
else:print("?")