#뮤직비디오
n,k = map(int,input().split())
a = list(map(int,input().split()))

def Count(capacity):
    cnt = 1
    sum = 0 
    for x in a:
        if sum+x > capacity:
            cnt += 1
            sum = x
        else:
            sum+=x
    return cnt

lt =  1
rt = sum(a)
res = 0
maxx=max(a)

while lt <= rt:
    mid = (lt+rt)//2
    if mid>=maxx and Count(mid)<=k:
        res = mid
        rt = mid -1
    else:
        lt = mid + 1
print(res)


        

