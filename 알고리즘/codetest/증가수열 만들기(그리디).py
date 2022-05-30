#증가수열 만들기(그리디)
from collections import deque
n = int(input())
a = list(map(int,input().split()))
deq= deque(a)
lt = 0
rt = n-1
anw= ''
while deq:
    if a[lt]<a[rt]:
        anw+='L'
        deq.popleft()
    if a[lt]>a[rt]:
        anw+='R'
        deq.pop()
print(anw)

