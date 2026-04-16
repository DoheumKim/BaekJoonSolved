cur_t = input().split()
cur_t = [int(cur_t[0]),int(cur_t[1])]
cook_t = int(input())
for i in range(cook_t):
    if cur_t[1] == 59:
        cur_t[1] = 0
        if cur_t[0] == 23:
            cur_t[0] = 0
        else:
            cur_t[0] += 1
    else:
        if cur_t[0] == 23:
            if cur_t[1] == 59:
                pass
            else:
                cur_t[1] += 1
        else:
            cur_t[1] += 1
print(f'{cur_t[0]} {cur_t[1]}')