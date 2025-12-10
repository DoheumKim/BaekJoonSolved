import sys
read = sys.stdin.readline()
s,sum=int(),0
print(read)
for i in read:
    s = ord(i)-30
    sum+= s
    print(i, end=' ')
print(sum)