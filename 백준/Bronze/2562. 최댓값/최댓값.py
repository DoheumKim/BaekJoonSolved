lst = list(input() for _ in range(9))

for i in range(len(lst)):
    lst[i] = int(lst[i])
print(f'{max(lst)}\n{(lst.index(max(lst))+1)}')