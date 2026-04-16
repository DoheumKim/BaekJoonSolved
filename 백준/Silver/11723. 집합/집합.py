import sys

m = int(sys.stdin.readline())
s = 0

for _ in range(m):
    line = sys.stdin.readline().split()
    
    if len(line) == 1:
        command = line[0]
        if command == "all":s = (1 << 21) - 1
        else:s = 0
    else:
        command, x = line[0], int(line[1])
        if command == "add":s |= (1 << x)
        elif command == "remove":s &= ~(1 << x)
        elif command == "check":
            if s & (1 << x):sys.stdout.write("1\n")
            else:sys.stdout.write("0\n")
        elif command == "toggle":s ^= (1 << x)