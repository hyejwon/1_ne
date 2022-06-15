#이분 검색
n,k =map(int,input().split())
a = list(map(int,input().split()))
pl = 0
pr = n-1

a.sort()

while pl<=pr:
    pc = (pl+pr)//2
    if a[pc] == k:
        print(pc+1)
        break
    elif a[pc]<k:
        pl = pc+1
    else:
        pr = pc -1


