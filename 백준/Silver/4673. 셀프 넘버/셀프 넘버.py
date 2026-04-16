lst = set(range(1, 10001))
slv = set()

for i in range(1, 10001):       # i = 850       
    for j in str(i):            # j = "8", "5", "0"
        i += int(j)             # 850 + 8 + 5 + 0, i = 863
    slv.add(i)        # 생성자가 있는 숫자들

dap = sorted(lst - slv)
for i in dap:
    print(i)