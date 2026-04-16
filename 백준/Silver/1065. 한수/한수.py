def num(N):
    if N >= 100 and N < 1000:
        N = str(N)
        if int(N[0])-int(N[1]) == int(N[1])-int(N[2]):
            return(1)
        else:
            return(0)
    elif N == 1000:
        return(0)
N = int(input())
if N < 100:
    print(N)
else:
    cnt = 99
    for a in range(N-99):
        if num(a+100):
            cnt += 1
    print(cnt)