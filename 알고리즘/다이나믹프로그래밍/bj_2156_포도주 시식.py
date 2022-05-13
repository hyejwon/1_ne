#2156 포도주 시식
n = int(input())
a = [0]*(n+1)
d = [0]*(n+1)
for i in range(1,n+1):
    a[i] = int(input())
d[1] = a[1]
if n >=2: #초기화
    d[2] = a[1]+a[2]

for i in range(3,n+1):
    d[i] = d[i-1] #값 세개중 최대값 비교하기.
    d[i] = max(d[i],d[i-2]+a[i])
    d[i] = max(d[i],d[i-3]+a[i]+a[i-1])


print(d[n])