#카드 역배치(정올 기출)
a = []
for i in range(1,21):
    a.append(i)

for _ in range(10):
    n,m=map(int,input().split())
    a[n-1:m] = list(reversed(a[n-1:m]))

for x in a:
    print(x,end=' ')