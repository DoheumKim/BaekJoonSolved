import sys

n = int(sys.stdin.readline()) # 컴퓨터 수
v = int(sys.stdin.readline()) # 연결 쌍의 수

# 인접 리스트로 그래프 구현
graph = [[] for _ in range(n + 1)]
for _ in range(v):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
infected_count = 0

def dfs(now):
    global infected_count
    visited[now] = True
    
    for next_node in graph[now]:
        if not visited[next_node]:
            infected_count += 1
            dfs(next_node)

# 1번 컴퓨터부터 전파 시작
dfs(1)
print(infected_count)