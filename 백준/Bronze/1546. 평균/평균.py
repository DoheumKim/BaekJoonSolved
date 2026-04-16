c = int(input())
sc = input().split()
fsc = sc
if len(sc) == c:
    for i in range(len(sc)):
        sc[i] = int(sc[i])
        fsc[i] = sc[i]
    M = max(sc)
    for i2 in range(len(sc)):
        sc[i2] = sc[i2]/M*100

if sum(fsc)-sum(sc) <=10**-2 or sum(sc)-sum(fsc) <= 10**-2:
    print(sum(sc)/len(sc))