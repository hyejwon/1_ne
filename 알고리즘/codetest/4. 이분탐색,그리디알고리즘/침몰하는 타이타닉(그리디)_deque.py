#침몰하는 타이타닉(그리디)
#2명 이하
#무게제한 
from collections import deque

n,limit=map(int,input().split())
p = list(map(int,input().split()))
p.sort()
p=deque(p)
cnt=0
while p:
    if len(p) ==1: #마지막 한명이 남음 
        cnt+=1
        break
    if p[0]+p[-1]>limit:
        p.pop()#구명보트를 타고 탈출함
        cnt += 1
    else:
        p.popleft()#앞에 자료가 빠짐
        p.pop() #맨뒤 자료가 빠짐
        cnt+=1
print(cnt)
