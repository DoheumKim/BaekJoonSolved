import sys
word = sys.stdin.readline().strip()
croatian_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for alpha in croatian_alphabets:word = word.replace(alpha, '*')
print(len(word))