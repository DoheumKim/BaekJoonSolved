N = input()
if len(N) == 1:
    N = '0'+N
a,b,c = N[0],N[-1],0
d = ''
while True:
    if d == N:
        break
    if c == 0:
        d = str(eval(a+'+'+b))
        d = b+d[-1]
    elif c > 0:
        a = d[0]
        b = d[1]
        d = str(eval(a+'+'+b))
        d = b+d[-1]
    if len(d) < 2:
        d = '0'+d
    c += 1
print(c)