import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

def is_prime(num):
    if num <= 1:return False
    i = 2
    while i * i <= num:
        if num % i == 0:return False
        i += 1
    return True

prime_count = 0
for num in nums:
    if is_prime(num):prime_count += 1

print(prime_count)