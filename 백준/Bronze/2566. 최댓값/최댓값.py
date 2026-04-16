matrix=[[0] for _ in range(9)]

max_val = 0;max_loc=[0,0]
for i in range(len(matrix)):

    matrix[i] = (list(map(int,input().split())))


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if max_val <= matrix[i][j]:max_val=matrix[i][j];max_loc=[i+1,j+1]

print(max_val)
print(max_loc[0],max_loc[1])