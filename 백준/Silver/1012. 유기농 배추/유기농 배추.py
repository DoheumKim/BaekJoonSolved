import sys
# 재귀 깊이 제한 해제 (DFS 필수)
sys.setrecursionlimit(10000)

def dfs(x, y, m, n, graph):
    # 상하좌우 방향 설정
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 현재 위치 방문 처리 (배추를 뽑아버리는 효과)
    graph[y][x] = 0
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 범위 내에 있고 배추(1)가 있다면 이동
        if 0 <= nx < m and 0 <= ny < n:
            if graph[ny][nx] == 1:
                dfs(nx, ny, m, n, graph)

t = int(sys.stdin.readline())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    # 배추밭 초기화 (n행 m열)
    field = [[0] * m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        field[y][x] = 1
        
    worm_count = 0
    for i in range(m):
        for j in range(n):
            if field[j][i] == 1:
                dfs(i, j, m, n, field)
                worm_count += 1
                
    print(worm_count)