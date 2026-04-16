import sys

from collections import Counter

def solve():
    n_count = int(sys.stdin.readline())
    cards = sys.stdin.readline().split() 
    m_count = int(sys.stdin.readline())
    targets = sys.stdin.readline().split()
    card_counts = Counter(cards)

    results = [str(card_counts[target]) for target in targets]   
    sys.stdout.write(" ".join(results) + "\n")
solve()

