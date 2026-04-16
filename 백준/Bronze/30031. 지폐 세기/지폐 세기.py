import sys

cost = {136:1000, 142:5000,148:10000, 154:50000}
out = int()
for i in range(int(sys.stdin.readline())):
    x,_ = map(int, sys.stdin.readline().split())
    out+= cost[x]
print(out)