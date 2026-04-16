import sys
a = list(map(int,sys.stdin.readline().split(' ')));res=0
for i in a:res += i**2
print(res%10)