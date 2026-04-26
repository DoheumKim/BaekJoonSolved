import sys

input_data = sys.stdin.readline

T_str = input_data()
T = int(T_str)
ans = []

for _ in range(T):
    N = int(input_data())
    
    max_a = 0
    max_b = 0
    max_c = 0
    possible = True
    
    for i in range(1, N + 1):
        a, b, c, p = map(int, input_data().split())
        
        if possible:
            if a > max_a: max_a = a
            if b > max_b: max_b = b
            if c > max_c: max_c = c
            
            if max_a + max_b + max_c + i > p:possible = False
                
    if possible:ans.append("YES")
    else:ans.append("NO")

sys.stdout.write("\n".join(ans) + "\n")