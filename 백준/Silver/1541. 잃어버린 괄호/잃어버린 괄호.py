import sys

groups = sys.stdin.readline().strip().split('-')

# 각 그룹 내부의 + 연산 처리
results = []
for group in groups:
    # '00009' 같은 숫자를 int로 변환하면 자동으로 9가 됨
    total = sum(map(int, group.split('+')))
    results.append(total)

# 첫 번째 그룹의 합에서 나머지 그룹의 합들을 모두 뺌
answer = results[0]
for i in range(1, len(results)):
    answer -= results[i]

print(answer)