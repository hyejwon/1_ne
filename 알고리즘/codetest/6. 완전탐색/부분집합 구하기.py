#부분집합 구하기
'''
전위순회방식으로 출력하기

'''
def DFS(v):
    if v == n+1:#종착점 도달하는부분
        for i in range(1,n+1):
            if ch[i]==1:
                print(i,end=' ')
        
        print()

    else:
        ch[v]=1 #원소를 부분집합으로 사용
        DFS(v+1)
        ch[v]=0
        DFS(v+1)
        

if __name__ == "__main__":

    n =int(input())
    ch = [0]*(n+1)
    DFS(1)
