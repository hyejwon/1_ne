#재귀함수와 스택
def DFS(x):
    if x > 0:
        DFS(x-1)
        print(x, end=' ')
        #DFS(x-1)#새로운 함수의 매개변수로 전달 됨

if __name__ =="__main__":
    n = int(input())
    DFS(n)