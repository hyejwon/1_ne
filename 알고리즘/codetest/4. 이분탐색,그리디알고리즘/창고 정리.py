#창고 정리
#입력
n =int(input())
a = list(map(int,input().split()))
k = int(input())
a.sort()

for _ in range(k):
    a[0]+=1
    a[n-1]-=1
    a.sort()

print(a[n-1]-a[0])
