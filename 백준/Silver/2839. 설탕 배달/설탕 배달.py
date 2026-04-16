import sys

n = int(sys.stdin.readline())

bag_count = 0

while n >= 0:

    # 5kg 봉지로 나누어떨어지는지 우선 확인

    if n % 5 == 0:

        bag_count += (n // 5)

        print(bag_count)

        break

    

    # 5로 안 나누어떨어지면 3kg 봉지 하나를 사용

    n -= 3

    bag_count += 1

else:

    # n이 음수가 될 때까지 위 조건을 만족하지 못한 경우

    print(-1)

