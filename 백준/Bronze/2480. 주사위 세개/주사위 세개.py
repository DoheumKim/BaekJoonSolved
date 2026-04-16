a,b,c = sorted(map(int,input().split()))
if (a+b+c)/3 == a:
    print(10000+b*1000)
elif (a+b)/2 == a or (b+c)/2 == b:
    print(1000+b*100)
else:
    print(c*100)