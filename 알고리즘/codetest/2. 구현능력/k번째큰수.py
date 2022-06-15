n,k = map(int,input().split())
a = list(map(int,input().split()))
res=set()#중복 제거 
for i in range(n):
    for j in range(i+1,n):#중복 방지를 위해 
        for m in range(j+1,n):
            res.add(a[i]+a[j]+a[m])

res=list(res) #list화
res.sort(reverse=True)#내림차순 정렬
print(res[k-1])


