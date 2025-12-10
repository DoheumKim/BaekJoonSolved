"""
regex: A-Za-z0-9
입력:공백없이
1line - max: 15
총 5line, 각 line별 글자 수는 다를 수 있음
글자는 세로로 읽음
https://www.acmicpc.net/problem/10798
"""

from sys import stdin
TRY = 5;lst = list()
for _ in range(TRY):
    lst.append(list(stdin.readline().strip()))
for i in range(15):
    for j in lst:
        if i<len(j):print(j[i],end='')

lst2 = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['a', 'b', 'd'], ['d', 'e', 'f']]

# print(lst2[0][1])