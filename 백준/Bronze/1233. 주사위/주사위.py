import sys
s1, s2, s3 = map(int, sys.stdin.readline().split())
counts = [0] * 81
for i in range(1, s1 + 1):
    for j in range(1, s2 + 1):
        for k in range(1, s3 + 1):
            sum_val = i + j + k
            counts[sum_val] += 1

max_count = 0
answer = 0

for i in range(3, 81):
    if counts[i] > max_count:
        max_count = counts[i]
        answer = i

print(answer)