import sys

isbn = sys.stdin.readline().strip()
target_idx = 0
total_sum = 0

for i in range(13):
    if isbn[i] == '*':
        target_idx = i
        continue
    
    weight = 1 if i % 2 == 0 else 3
    total_sum += int(isbn[i]) * weight

target_weight = 1 if target_idx % 2 == 0 else 3

for x in range(10):
    if (total_sum + (x * target_weight)) % 10 == 0:
        print(x)
        break