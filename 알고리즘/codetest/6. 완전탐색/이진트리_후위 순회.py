#후위 순회-병합정렬 
def DFS(v):
    if v>7: #dfs는 기본적으로 if-else #노드값이 7까지 있음 
        return 
    else:
        DFS(v*2)#왼쪽 자식노드 -본연의 일
        DFS(v*2+1)#오른쪽 자식노드 
        print(v,end=" ")#함수 본연의 일(방문)        


if __name__=="__main__":
    DFS(1) #1번 부모 노드에서 출발 함 