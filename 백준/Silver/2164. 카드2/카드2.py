import sys
from collections import deque

n = int(sys.stdin.readline())
cards = deque(range(1, n + 1))

while len(cards) > 1:
    cards.popleft()
    if cards:
        top_to_bottom = cards.popleft()
        cards.append(top_to_bottom)
print(cards[0])