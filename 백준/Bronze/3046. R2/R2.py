import sys
R1,S=sys.stdin.readline().split()
R1,S=int(R1),int(S)
R2=0
if -1000 <= R1 <=1000 and -1000 <= S <=1000:
    R2=(S*2-R1)
print(R2)