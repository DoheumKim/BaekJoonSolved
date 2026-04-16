tc = int(input());out=''
for i in range(tc):inp = input();f,l=inp[0],inp[-1];out+=f;out+=l+'\n'
print(out.rstrip())