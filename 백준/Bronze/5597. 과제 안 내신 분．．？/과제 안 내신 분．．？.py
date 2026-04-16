lst = [i for i in range(1,31)]
for i in range(28):a=int(input());lst.remove(a)
print(f'{min(lst)}\n{max(lst)}')