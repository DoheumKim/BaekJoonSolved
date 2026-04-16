a = []
for i in range(10):
	a.append(int(input()))
	a[i] = a[i]%42
	
b = set(a)
print(len(a)-(len(a)-len(b)))