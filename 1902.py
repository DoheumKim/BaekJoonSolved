'''입력 받기: N개의 동굴 바닥 꼭짓점 좌표를 입력받습니다.

상부 볼록 껍질(Upper Convex Hull) 구하기:

주어진 N개의 점들로 상부 볼록 껍질을 구성하는 점들을 찾습니다. 이는 보통 '그레이엄 스캔(Graham Scan)'이나 '모노톤 체인(Monotone Chain)' 알고리즘을 변형하여 구현할 수 있습니다.

점들을 X좌표 순으로 순회하면서, 스택을 이용해 이전 점들과의 기울기를 비교하여 "오른쪽으로 꺾이는" 형태를 유지하도록 점들을 추가/제거하면 상부 볼록 껍질을 만들 수 있습니다.

최소 높이 계산하기:

최종 답이 될 min_height 변수를 매우 큰 값으로 초기화합니다.

입력으로 주어진 모든 동굴 꼭짓점 $t_i = (X_i, Y_i)$에 대해 다음을 반복합니다.

현재 X좌표 X 
i
​
 에서 상부 볼록 껍질의 높이 $Hull(X_i)$를 계산합니다. (볼록 껍질을 이루는 선분 중 X 
i
​
 를 포함하는 선분을 찾아 직선의 방정식을 이용해 높이를 구합니다.)

해당 X좌표에서 램프가 있어야 할 최소 높이는 max(Y 
i
​
 ,Hull(X 
i
​
 )) 입니다.

이 값을 min_height와 비교하여 더 작은 값으로 업데이트합니다. min_height = min(min_height, max(Y_i, Hull(X_i)))

결과 출력: 계산된 min_height 값을 소수점 둘째 자리까지 출력합니다.
'''
import sys
N = sys.stdin.readline()
# print(N)
for _ in range(int(N)):
    x, y = map(int, sys.stdin.readline().split())
    print(x, y)
