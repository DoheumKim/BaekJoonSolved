import sys
from collections import Counter

# 반올림
round_fn = lambda val: int(val + 0.5) if val >= 0 else int(val - 0.5)

n = int(sys.stdin.readline())
nums = sorted([int(sys.stdin.readline()) for _ in range(n)])

# 산술평균
print(round_fn(sum(nums) / n))
# 중앙값
print(nums[n // 2])
# 최빈값
counts = Counter(nums).most_common()
if len(counts) > 1 and counts[0][1] == counts[1][1]:
    # 최빈값이 여러 개라면 두 번째로 작은 값 출력
    print(counts[1][0])
else:
    print(counts[0][0])
# 범위
print(nums[-1] - nums[0])