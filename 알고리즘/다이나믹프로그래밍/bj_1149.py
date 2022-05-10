#RGB거리
n = int(input())
a = [(0,0,0)]+[tuple(map(int,input().split())) for _ in range(n)]#비용
d = [[0,0,0] for _ in range(n+1)]

for j in range(1,n+1):
    d[j][0] = min(d[j-1][1],d[j-1][2])+a[j][0]
    d[j][1] = min(d[j-1][0],d[j-1][2])+a[j][1]
    d[j][2] = min(d[j-1][0],d[j-1][1])+a[j][2]

print(min(d[n][0],d[n][1],d[n][2]))