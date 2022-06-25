
def DFS(L,sum):#sum은 부분집합의 합
    global result#main 함수에 있는 변수 가져옴 
    if sum > c :
        return
    if L== n:#말단노드인 종료지점이 옴
        if sum >result:
            result=sum
    else:
        DFS(L+1,sum+a[L])
        DFS(L+1,sum)
    

if __name__ == "__main__":
    c,n = map(int,input().split())
    a = [0]*n #바둑이의 몸무게
    result = -2147000000 
    for i in range(n):
        a[i] = int(input())
    DFS(0,0)
    print(result)

"""
cut edge tech
def DFS(L, sum, tsum):
    global result
    if sum+(total-tsum)<result:
        return
    if sum>c:
        return
    if L==n:
        if sum>result:
            result=sum
    else:
        DFS(L+1, sum+a[L], tsum+a[L])
        DFS(L+1, sum, tsum+a[L])

if __name__=="__main__":
    c, n=map(int, input().split())
    a=[0]*n
    result=-2147000000
    for i in range(n):
        a[i]=int(input())
    total=sum(a)
    DFS(0, 0, 0)
    print(result)

"""
