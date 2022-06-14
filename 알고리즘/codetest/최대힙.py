#최대힙 
#부모 노드가 자식 노드보다 항상 커야함
#heapq는 기본적으로 최소힙
#음수 처리 
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
            print(-hq.heappop(a))#루트 노드값이 나옴
    else:
        hq.heappush(a,-n)
        
        