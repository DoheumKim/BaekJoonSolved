import sys
from collections import deque

# 재귀 깊이 제한 (DFS용)
sys.setrecursionlimit(10**6)

def dfs(v, adj, visited):
    visited[v] = True
    print(v, end=' ')
    for i in sorted(adj[v]):
        if not visited[i]:
            dfs(i, adj, visited)

def bfs(start, adj, n):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in sorted(adj[v]):
            if not visited[i]:
                visited[i] = True
                queue.append(i)

n, m, v = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    adj[s].append(e)
    adj[e].append(s)

# DFS 실행
visited_dfs = [False] * (n + 1)
dfs(v, adj, visited_dfs)
print() # 줄바꿈

bfs(v, adj, n)