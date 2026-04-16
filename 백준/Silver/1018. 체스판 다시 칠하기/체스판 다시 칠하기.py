import sys

n, m = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(n)]
min_repaint = 64

# 8x8로 자를 수 있는 모든 시작 범위 탐색
for i in range(n - 7):
    for j in range(m - 7):
        case_w = 0 # 맨 왼쪽 위가 'W'인 경우
        case_b = 0
        
        # 8x8 영역 검사
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:
                    if board[x][y] != 'W': case_w += 1
                    if board[x][y] != 'B': case_b += 1
                else:
                    if board[x][y] != 'B': case_w += 1
                    if board[x][y] != 'W': case_b += 1
        
        min_repaint = min(min_repaint, case_w, case_b)

print(min_repaint)