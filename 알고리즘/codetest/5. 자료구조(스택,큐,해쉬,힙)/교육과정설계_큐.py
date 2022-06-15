from collections import deque
need=input()
n=int(input())
for i in range(n):
    plan = input()
    dq = deque(need)
    for x in plan:
        if x in dq:#패턴을 하나 만들기
            if x!=dq.popleft():#순서가 어긋남
                print("#%d NO" %(i+1))
                break
    else:#순서가 통과됨
        if len(dq)==0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))
                 

