import sys

from collections import deque

n, k = map(int, sys.stdin.readline().split())
people = deque(range(1, n + 1))
sequence = []

while people:

    # K-1번 동안 맨 앞 사람을 뒤로 보냄 (회전)
    for _ in range(k - 1): people.append(people.popleft())
    # K번째 사람을 제거하여 순열에 추가
    sequence.append(str(people.popleft()))

# 양식에 맞춰 출력
print("<" + ", ".join(sequence) + ">")

