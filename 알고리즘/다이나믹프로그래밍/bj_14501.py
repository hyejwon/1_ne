#퇴사- d[day]의 각각의 최댓값이 전체의 최댓값이 된다.->dp
inf = 10**9
n = int(input())
t = [0]*(n+1)
p = [0]*(n+1)
d = [-1]*(n+1) #메모이제이션 리스트 

for i in range(1,n+1):
    t[i],p[i] = map(int,input().split())
ans = 0
def go(day):
    if day == n+1: #재귀함수 종료조건
        return 0
    if day > n+1:
        return -inf
    if d[day] != -1:#초기값이 아닌경우 d[day]
        return d[day]
    t1 =  go(day+1)
    t2 = p[day]+go(day+t[day])
    d[day] = max(t1,t2)
    return d[day]

print(go(1))