n =int(input())
a = [list(map(int,input().split())) for _ in range(n) ]
m = int(input())

#회전하기
for j in range(m):
    i,l,k = map(int,input().split())
    if l == 0:#왼쪽 방향
        for _ in range(k):
            a[i-1].append(a[i-1].pop(0)) 
    else:
        for _ in range(k):
            a[i-1].insert(0,a[i-1].pop())

s=0
e=n-1
sum=0

for i in range(n):
    for j in range(s,e+1):
        sum+=a[i][j] 
    if i < n//2:
        s +=1
        e -=1
    else :
        s-=1
        e+=1

print(sum)

