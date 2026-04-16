import sys

n = int(sys.stdin.readline())
res = 0
for i in range(1, n + 1):
    digit_sum = sum(map(int, str(i)))
    decomposition_sum = i + digit_sum
    if decomposition_sum == n:
        res = i
        break
        
print(res)