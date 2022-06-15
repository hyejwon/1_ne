#재귀함수를 이용한 이진수 출력
ans =''
def DFS(x): #깊이 우선 탐색
    if x==0:
        return # 함수를 종료 

    else:
        DFS(x//2)
        print(x%2, end='')
if __name__=="__main__":
    n = int(input())
    DFS(n)