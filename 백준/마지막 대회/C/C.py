import sys
from bisect import bisect_right

input_data = list(map(int, sys.stdin.read().split()))
N = input_data[0];D = input_data[1]
dishes = [];idx = 2;ans = 0

for _ in range(N):
    t = input_data[idx]
    a = input_data[idx+1]
    b = input_data[idx+2]
    idx += 3
    
    dishes.append((t, a, b))
    
    # 요리를 1개만 만들었을 때의 최댓값 갱신
    if a + b > ans:ans = a + b

# 시간을 기준으로 오름차순 정렬
dishes.sort(key=lambda x: x[0])

# 이분 탐색을 위한 시간 배열 분리
T_arr = [d[0] for d in dishes]

# 누적 최댓값 (Prefix Max) 배열 생성
# pref_A[i] : 0번부터 i번까지 요리 중 A의 최댓값
pref_A = [0] * N;pref_B = [0] * N
pref_A[0] = dishes[0][1];pref_B[0] = dishes[0][2]

for i in range(1, N):
    pref_A[i] = pref_A[i-1] if pref_A[i-1] > dishes[i][1] else dishes[i][1]
    pref_B[i] = pref_B[i-1] if pref_B[i-1] > dishes[i][2] else dishes[i][2]

# 2. 요리를 2개 만들 때의 최댓값 탐색
for j in range(1, N):
    t_j = dishes[j][0]
    a_j = dishes[j][1]
    b_j = dishes[j][2]
    
    # j번 요리를 만들고 남은 시간
    rem = D - t_j
    
    # 남은 시간으로 만들 수 있는 요리가 아예 없다면
    if rem < T_arr[0]:continue
        
    # 남은 시간 이내에 만들 수 있는 가장 오래 걸리는 요리의 인덱스 탐색
    k = bisect_right(T_arr, rem) - 1
    
    # j번 요리 자신과 중복해서 2번 만들 수는 없으므로, k를 j-1로 제한
    # (i, j 위치가 바뀌는 경우는 어차피 반복문이 돌면서 다 체크됨)
    if k >= j:k = j - 1
        
    if k >= 0:
        # A점수를 0~k 구간의 최댓값으로, B점수를 j번 요리로 할 때
        score1 = pref_A[k] + b_j
        if score1 > ans:ans = score1
            
        # A점수를 j번 요리로, B점수를 0~k 구간의 최댓값으로 할 때
        score2 = a_j + pref_B[k]
        if score2 > ans:ans = score2

print(ans)