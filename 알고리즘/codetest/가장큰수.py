num,m = map(int,input().split())
num = list(map(int,str(num)))#문자열
stack = []
for x in num:
    while stack and m>0 and stack[-1]<x:#stack이 비어있으면 멈춤 
        stack.pop()
        m-=1
    stack.append(x)
#다 지우지 못하는 경우.
if m!=0:
    stack=stack[:-m]
res=''.join(map(str,stack))
print(res)
#for i in stack:
#    print(i,end='')
