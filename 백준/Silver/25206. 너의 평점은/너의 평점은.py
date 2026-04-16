import sys
N=20;score=int()
total_score = 0.0   # 학점 * 평점
total_credits = 0.0

scoreboard = {'A+':4.5, 'A0':4.0, 'B+': 3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0,'D+':1.5, 'D0':1.0, 'F':0.0}
for _ in range(N):
    line = sys.stdin.readline().split()
    if not line: break # 입력이 끝날때
    
    name, credit, grade = line
    credit = float(credit)
    
    if grade != 'P':
        total_score += credit * scoreboard[grade]
        total_credits += credit
# 적어도 한 과목은 P가 아님 -> division by zero 해결
print(f"{total_score / total_credits:.6f}")
    

