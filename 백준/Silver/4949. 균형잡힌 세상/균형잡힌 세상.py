import sys

def check_balance(text):

    stack = []

    

    # 괄호 짝을 매핑하여 가독성 향상

    matching_pairs = {')': '(', ']': '['}

    

    for char in text:

        if char in '([':

            stack.append(char)

        elif char in ')]':

            # 스택이 비었거나 짝이 맞지 않는 경우

            if not stack or stack.pop() != matching_pairs[char]:

                return "no"

                

    # 모든 검사 후 스택이 완전히 비어있어야 균형 잡힌 것

    return "yes" if not stack else "no"

while True:

    line = sys.stdin.readline().rstrip('\n')

    

    # 종료 조건: 온점 하나만 들어온 경우

    if line == ".":

        break

        

    print(check_balance(line))

