import sys

s = [sys.stdin.readline().strip() for _ in range(3)]
next_num = 0

for i in range(3):
    if s[i] not in ["Fizz", "Buzz", "FizzBuzz"]:
        next_num = int(s[i]) + (3 - i)
        break

if next_num % 3 == 0 and next_num % 5 == 0:
    print("FizzBuzz")
elif next_num % 3 == 0:
    print("Fizz")
elif next_num % 5 == 0:
    print("Buzz")
else:
    print(next_num)