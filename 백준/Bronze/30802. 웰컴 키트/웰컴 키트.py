import sys

n = int(sys.stdin.readline())
sizes = list(map(int, sys.stdin.readline().split()))
t, p = map(int, sys.stdin.readline().split())

total_t_bundles = 0
for s in sizes:
    if s == 0:continue
    total_t_bundles += (s - 1) // t + 1

p_bundles = n // p
p_singles = n % p

print(total_t_bundles)
print(f"{p_bundles} {p_singles}")