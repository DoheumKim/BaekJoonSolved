import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

u_count = s.count('u')
o_count = s.count('o')
s_count = s.count('s')
p_count = s.count('p')
c_count = s.count('c')

result = min(u_count, o_count, s_count, p_count, c_count)

print(result)