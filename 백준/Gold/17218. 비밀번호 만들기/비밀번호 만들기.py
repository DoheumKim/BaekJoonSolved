import sys

# 두 문자열 입력 받기
input_data = sys.stdin.read().split()
if not input_data:
    exit()

A, B = input_data[0], input_data[1]

# 2차원 DP 배열 생성 (문자열을 직접 저장)
dp = [[""] * (len(B) + 1) for _ in range(len(A) + 1)]

for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i-1] == B[j-1]:
            # 문자가 같으면 이전 공통 부분에 현재 문자 추가
            dp[i][j] = dp[i-1][j-1] + A[i-1]
        else:
            # 다르면 이전까지 구한 부분 문자열 중 더 긴 것을 계승
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

# 배열의 가장 마지막 값이 최장 공통 부분 문자열
print(dp[-1][-1])