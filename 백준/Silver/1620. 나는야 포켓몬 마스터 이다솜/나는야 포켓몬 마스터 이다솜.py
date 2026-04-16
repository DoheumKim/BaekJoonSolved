import sys

n, m = map(int, sys.stdin.readline().split())
name_to_id = {}
id_to_name = {}

for i in range(1, n + 1):
    name = sys.stdin.readline().strip()
    name_to_id[name] = i
    id_to_name[i] = name

for _ in range(m):
    query = sys.stdin.readline().strip()
    
    if query.isdigit():
        sys.stdout.write(id_to_name[int(query)] + '\n')
    else:
        sys.stdout.write(str(name_to_id[query]) + '\n')