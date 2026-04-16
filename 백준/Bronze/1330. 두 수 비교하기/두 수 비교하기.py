A,B=input().split()
A,B=int(A),int(B)
if -10000<=A and B<=10000:
    if A>B:
        print('>')
    elif A<B:
        print('<')
    elif A==B:
        print('==')