#11055_가장 큰 증가하는 부분수열
n = int(input())
a=list(map(int,input().split()))
d = [0]*n
for i in range(n):
    d[i]=a[i]
    for j in range(0,i):
        if a[j]<a[i] and d[i]<d[j]+a[i] :
            d[i]=d[j]+a[i]
print(max(d))