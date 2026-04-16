import sys

while True:
    line = sys.stdin.readline().rstrip('\n')
    
    if line == '#':break

    line = line.lower()
    count = 0
    for char in line:
        if char in 'aeiou':count += 1
    print(count)