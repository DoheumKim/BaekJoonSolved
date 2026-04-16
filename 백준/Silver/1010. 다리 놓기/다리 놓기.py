import sys
import math

input_data = sys.stdin.read().split()
if not input_data:
    exit()

T = int(input_data[0])
idx = 1
ans = []

for _ in range(T):
    N = int(input_data[idx])
    M = int(input_data[idx+1])
    idx += 2
    
    # M개 중에서 N개를 순서 없이 고르는 조합(Combination) 계산
    ans.append(str(math.comb(M, N)))

sys.stdout.write("\n".join(ans) + "\n")