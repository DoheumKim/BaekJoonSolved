import sys

while True:
    line = sys.stdin.readline().strip()
    if line == "0": break
    
    res = line
    while len(str(res)) > 1:
        res = sum(int(digit) for digit in str(res))
    
    print(res)