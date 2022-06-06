s = input()
stack=[]
cnt=0
for i in range(len(s)):
    if s[i]=='(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1]=='(':#레이저
            cnt += len(stack)
        else:#쇠막대기의 끝
            #쇠막대기 시작 제거 
            cnt+=1
print(cnt)
