import sys
N = int(sys.stdin.readline())
for i in sorted(int(sys.stdin.readline()) for _ in range(N)):
   sys.stdout.write(f"{i}\n")