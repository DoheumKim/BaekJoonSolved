import sys

def solve():
    input_count = int(sys.stdin.readline())
    ledger = []

    for _ in range(input_count):
        number = int(sys.stdin.readline())

        if number == 0:
            ledger.pop()
        else:ledger.append(number)
            
    print(sum(ledger))

solve()

