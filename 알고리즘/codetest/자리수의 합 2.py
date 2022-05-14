#자리수의 합 2 
n = int(input())
a = list(map(int,input().split()))
def digit_sum(x):
    sum = 0
    for i in str(x):#문자열로 바꾼후
        sum+= int(i)#합에는 int화 해준다
    return sum
max = -2147000000
for x in a:
    tot= digit_sum(x)
    if tot >max:
        max = tot
        res = x

print(res)
