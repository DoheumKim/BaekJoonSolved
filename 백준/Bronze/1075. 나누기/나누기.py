import sys
n = int(sys.stdin.readline())
f = int(sys.stdin.readline())
base_n = (n // 100) * 100

for i in range(100):
    current_n = base_n + i
    if current_n % f == 0:
        print(f"{i:02}")
        break