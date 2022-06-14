a=input()
stack=[]
res = ''
for x in a:
    if x.isdecimal():
        res+=x #누적
    else:
        if x =='(':
            stack.append(x)
        elif x =='*' or x =='/':
            while stack and (stack[-1]=='*'or stack[-1]=='/'):
                res+=stack.pop() #끄집어냄 
            stack.append(x)
        elif x =='+' or x=='-':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.append(x)
        elif x ==')':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.pop()

while stack:#stack에 남아 있는게 있는 경우  
    res+=stack.pop()

print(res)


