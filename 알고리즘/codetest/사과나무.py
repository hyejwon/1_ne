n =int(input())
a = [list(map(int,input().split())) for _ in range(n) ]
res = 0
s = e = n//2

for i in range(n):
    for j in range(s, e+1): #s부터 e까지 돌아야함 
        res+=a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else: 
        s+=1
        e-=1
 