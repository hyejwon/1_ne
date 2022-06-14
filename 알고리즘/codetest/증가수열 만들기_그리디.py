#증가수열 만들기(그리디)
#from collections import deque
n = int(input())
a = list(map(int,input().split()))
lt = 0
rt = n-1
last = 0
res = ""
tmp = []
while lt<=rt:
    if a[lt]>last:
        tmp.append((a[lt],'L'))

    if a[rt]>last:        
        tmp.append((a[rt],'R'))
    tmp.sort()#튜플의 첫 자료 기준 정렬

    if len(tmp)==0:
        break
    else:
        res=res+tmp[0][1]
        last=tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    tmp.clear()

print(len(res))
print(res)

