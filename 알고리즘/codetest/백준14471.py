n,m=map(int,input().split())
cnt=0
least=[]
for _ in range (m):
    ai,bi=map(int, input().split())
    if ai>=n: cnt+=1
    else: least.append( (n-ai));
least=sorted(least)
if cnt >= m-1: print(0)
else: print(sum(least[:m-cnt-1]))