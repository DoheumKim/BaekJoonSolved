import sys

n = int(sys.stdin.readline())
a = set(map(int, sys.stdin.readline().split())) # set는 해쉬테이블 쓰므로 탐색시간 O(1)
m = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

for i in targets:
    if i in a:sys.stdout.write("1\n")
    else:sys.stdout.write("0\n")