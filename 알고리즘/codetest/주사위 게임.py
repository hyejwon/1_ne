#주사위 게임
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
    