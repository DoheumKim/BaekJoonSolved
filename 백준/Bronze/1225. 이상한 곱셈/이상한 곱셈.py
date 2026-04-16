import sys
a,b = sys.stdin.readline().split()
sum_a = sum(int(i) for i in a)
sum_b = sum(int(i) for i in b)
print(sum_a * sum_b)