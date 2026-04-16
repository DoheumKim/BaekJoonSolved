import sys

n_input = sys.stdin.readline().strip()
if not n_input:exit()
N = int(n_input)

files = []
for _ in range(N):files.append(sys.stdin.readline().strip())

pattern = list(files[0]);length = len(pattern)

for i in range(1, N):
    for j in range(length):
        if pattern[j] != files[i][j]:pattern[j] = '?'

print("".join(pattern))