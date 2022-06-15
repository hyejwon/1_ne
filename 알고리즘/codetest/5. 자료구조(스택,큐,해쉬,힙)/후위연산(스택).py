a=input()
stack=[]
for x in a:
    if x.isdecimal():
        stack.append(int(x))#실제 숫자가 들어가게 함     
    else:
        if x=='+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)
        elif x=='-':
            a = stack.pop()
            b = stack.pop()
            stack.append(a-b)
        elif x=='*':
            a = stack.pop()
            b = stack.pop()
            stack.append(b*a)
        elif x=='/':
            a = stack.pop()
            b = stack.pop()
            stack.append(b/a)
print(stack[0])