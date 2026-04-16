H,M=input().split()
H,M=int(H),int(M)
if 0<=H<=23 and 0<=M<=59:
    
    if M>=15:
        if M==45:
            M=0
        elif M>45:
            M-=45
        else:
            M+=15
            if H==0:
                H=23
            else:
                H-=1
    else:
        M+=15
        if H!=0:
            H-=1
        else:
            H=23
print(H,M)