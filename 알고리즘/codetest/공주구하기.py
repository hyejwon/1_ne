from collections import deque

#공주구하기
n,k = map(int,input().split())
dq =list(range(1,n+1))
dq=deque(dq)

while dq:
    for _ in range(k-1):#반복만
        cur=dq.popleft()
        dq.append(cur)
    dq.popleft() #k번째 
    if len(dq)==1:
        print(dq[0])
        dq.popleft()


