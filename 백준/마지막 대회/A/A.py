# 이렇게 떠나는구나..
import sys

N = int(sys.stdin.readline().strip())

rows = 2 * N;cols = 4 * N + 2

for i in range(rows):
    line = [' '] * cols
    
    # 1번 별
    p1 = 2 * N - 1 - i
    
    # 2번, 3번 별
    if i < N:
        p2 = 3 * N - i
        p3 = 3 * N + 2 + i
    else:
        p2 = N + i + 1
        p3 = 5 * N - i + 1
        
    if 0 <= p1 < cols: line[p1] = '*'
    if 0 <= p2 < cols: line[p2] = '*'
    if 0 <= p3 < cols: line[p3] = '*'
    
    # 리스트를 문자열로 합치고, 문제 조건대로 공백 유지하며 출력
    sys.stdout.write("".join(line) + "\n")