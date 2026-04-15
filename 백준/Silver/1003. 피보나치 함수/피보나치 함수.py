import sys

input_data = sys.stdin.read().split()
if not input_data:exit()

T = int(input_data[0]);queries = list(map(int, input_data[1:]))

zero_count = [0] * 41;one_count = [0] * 41
zero_count[0], one_count[0] = 1, 0;zero_count[1], one_count[1] = 0, 1

for i in range(2, 41):
    zero_count[i] = zero_count[i-1] + zero_count[i-2]
    one_count[i] = one_count[i-1] + one_count[i-2]

for n in queries:print(f"{zero_count[n]} {one_count[n]}")