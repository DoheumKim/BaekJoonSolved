import sys
N = int(sys.stdin.readline())
group_word_count = 0

for _ in range(N):
    word = sys.stdin.readline().strip()
    visited = []
    is_group_word = True
    
    for i in range(len(word)):
        if word[i] not in visited:visited.append(word[i])
        else:
            if word[i] != word[i-1]:
                is_group_word = False
                break
    
    if is_group_word:group_word_count += 1
print(group_word_count)