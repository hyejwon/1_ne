#주사위 게임
<<<<<<< HEAD
def reward(x):
    #for i in range(len(x)):
    sum=0 #초기화
    if (x[0]==x[1]) and (x[1]==x[2]) and (x[0]==x[2]):
        sum = 10000+(x[0]*1000)
    elif (x[0]==x[1]) or (x[0]==x[2]):     
        sum = 1000+x[0]*100
    elif (x[1]==x[2]):
        sum = 1000+x[1]*100
    else :
        sum= max(x)*100
    return sum

n = int(input())
#for i in range(n):
#    tmp=input().split
#    tmp.sort()
#    a,b,c =map(int,tmp)
#    if a==b and b==c:
#        money = 10000+a*1000
#    elif a==b or a==c:
#        money = 1000+(a*100)



a= [list(map(int,input().split())) for i in range(n)] 
    
print(max(reward(a[0]),reward(a[1]),reward(a[2])))
=======
n = int(input())
max = 0
for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c =map(int,tmp)
    if a ==b and b==c: #가장 구하고 싶은 조건 
        sum=10000+(a*1000)
    elif a == b or a == c:
        sum = 1000+(a*100)
    elif b == c :
        sum = 1000+(b*100)
    else:
        sum = c *100
    
    if sum>max:
        max = sum
print(max)
    
>>>>>>> 6f115085c2d78cd51bdc458a4f4a9be20e2a5da7
