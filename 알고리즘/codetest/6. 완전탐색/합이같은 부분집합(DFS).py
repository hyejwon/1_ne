#합이같은 부분집합
'''
전체 원소의 합 total
부분집합을 만들어서 sum에 누적
sum == total-sum # total-sum은 새로 만든 부분집합 에서 뺀 나머지 부분집합
 
'''
def DFS(L,sum):
    if sum > total //2:
        return
        
    if L ==n:
        if sum ==(total-sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input.split()))
    total = sum(a)
    DFS(0,0)
    print("No")