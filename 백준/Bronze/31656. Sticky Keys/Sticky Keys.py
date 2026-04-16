import sys

s = sys.stdin.readline().rstrip('\n')

if not s:
    print("")
else:
    result = [s[0]]
    for i in range(1, len(s)):
        if s[i] != s[i-1]:result.append(s[i])
    print("".join(result))