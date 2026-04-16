import sys
me,c,p = (int(sys.stdin.readline()) for _ in range(3))
print('no' if me > c*p else 'yes')