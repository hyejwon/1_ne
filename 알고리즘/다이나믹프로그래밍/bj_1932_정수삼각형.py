#정수삼각형_1932
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
d = [[0]*n for _ in range(n)]
d[0][0]=a[0][0] #맨 위 값으로 초기화 
for i in range(1,n):
    for j in range(0,i+1):
        d[i][j] = d[i-1][j]+a[i][j]#오른쪽 대각선 
        if j-1 >=0 and d[i][j] <d[i-1][j-1] +a[i][j]:#왼쪽 대각선이 더 큰 경우
            d[i][j] =d[i-1][j-1]+a[i][j]

print(max(d[n-1]))#0부터 행을 셌으므로 n-1 d[n]하면 리스트 범위 에러

