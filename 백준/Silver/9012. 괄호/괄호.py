import sys

n = int(sys.stdin.readline())

for _ in range(n):
    text = sys.stdin.readline().strip()
    count = 0
    is_vps = True
    
    for char in text:
        if char == '(':count += 1
        elif char == ')':count -= 1
        
        # 중간에 닫는 괄호가 더 많아지면 즉시 실패
        if count < 0:
            is_vps = False
            break
    
    # 끝났을 때 count가 정확히 0이어야 함
    if is_vps and count == 0:sys.stdout.write("YES\n")
    else:sys.stdout.write("NO\n")