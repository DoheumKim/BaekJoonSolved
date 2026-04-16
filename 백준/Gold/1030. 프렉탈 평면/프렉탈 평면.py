import sys

s, n, k, r1, r2, c1, c2 = map(int, sys.stdin.readline().split())

def is_black(size, r, c):
    if size == 1:return 0
    prev_size = size // n
    black_start = (n - k) // 2
    black_end = black_start + k
    
    if black_start <= r // prev_size < black_end and \
       black_start <= c // prev_size < black_end:return 1
    
    return is_black(prev_size, r % prev_size, c % prev_size)

total_size = n ** s

for i in range(r1, r2 + 1):
    row = ""
    for j in range(c1, c2 + 1):row += str(is_black(total_size, i, j))
    print(row)