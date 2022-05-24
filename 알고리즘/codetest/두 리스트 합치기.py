#두 리스트 합치기
n = int(input())
a = list(map(int,input().split()))
n2 = int(input())
b = list(map(int,input().split()))
c = a+b
c.sort()
for i in range(n+n2):
    print(c[i],end=' ')