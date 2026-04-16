import sys

t = int(sys.stdin.readline())

for i in range(1, t + 1):
    n, m = map(int, sys.stdin.readline().split())
    # 등차수열의 합 공식
    total_sum = (n + m) * (m - n + 1) // 2
    # 출력 양식
    print(f"Scenario #{i}:")
    print(total_sum)
    # 마지막 케이스가 아닐 때만 빈 줄 출력
    if i != t: print()