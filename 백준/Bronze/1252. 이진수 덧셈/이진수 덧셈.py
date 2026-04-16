import sys
line = sys.stdin.readline().split()
if line:
    a_str, b_str = line
    a_int = int(a_str, 2);b_int = int(b_str, 2)
    added_val = a_int + b_int
    res = format(added_val, 'b')
    print(res)