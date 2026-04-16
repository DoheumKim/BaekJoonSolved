import sys

n = int(sys.stdin.readline())

words = []

for _ in range(n):

    words.append(sys.stdin.readline().strip())

# set을 이용한 중복 제거 후 다시 리스트로 변환

words = list(set(words))

# 정렬 기준: 1순위 길이를 나타내는 len(x), 2순위 문자열 자체인 x

words.sort(key=lambda x: (len(x), x))

for word in words:

    sys.stdout.write(word + '\n')

