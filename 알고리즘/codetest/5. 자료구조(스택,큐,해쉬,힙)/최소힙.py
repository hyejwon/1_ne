import heapq as hq
a = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a)==0:#힙의 자료구조가 없음
            print(-1)
        else:
            print(hq.heappop(a))#루트 노드값이 나옴
    else:
        hq.heappush(a,n)
        

