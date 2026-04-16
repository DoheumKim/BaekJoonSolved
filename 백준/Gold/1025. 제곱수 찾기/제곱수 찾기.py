import sys

n, m = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(n)]
ans = -1

def is_perfect_square(num):
    if num < 0: return False
    root = int(num ** 0.5)
    return root * root == num

for r in range(n):
    for c in range(m):
        for dr in range(-n + 1, n):
            for dc in range(-m + 1, m):
                if dr == 0 and dc == 0:
                    num = int(board[r][c])
                    if is_perfect_square(num):
                        ans = max(ans, num)
                    continue
                
                curr_r, curr_c = r, c
                num_str = ""
                
                while 0 <= curr_r < n and 0 <= curr_c < m:
                    num_str += board[curr_r][curr_c]
                    val = int(num_str)
                    
                    if is_perfect_square(val):ans = max(ans, val)
                    
                    curr_r += dr
                    curr_c += dc
print(ans)