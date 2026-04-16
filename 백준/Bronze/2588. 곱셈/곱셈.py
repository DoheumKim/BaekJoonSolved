a = int(input())

b = int(input())
b = str(b)
for i in range(1,4):
    print(a * int(b[-i]))
print(a*int(b))