import sys

a, b = map(int, sys.stdin.readline().split())
def get_gcd(a, b):
    while b > 0:a, b = b, a % b
    return a
gcd = get_gcd(a, b)
lcm = (a * b) // gcd

print(gcd)
print(lcm)