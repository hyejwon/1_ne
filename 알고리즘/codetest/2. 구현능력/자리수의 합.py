#자리수의 합 1 
n = int(input())
a = list(map(int,input().split()))
def digit_sum(x):
    sum = 0
    while x >0:
        sum+=x%10 #x를 10으로 나눈 나머지 
        x=x//10 #x를 10으로 나눈 몫
    return sum
max = -2147000000
for x in a:
    tot= digit_sum(x)
    if tot >max:
        max = tot
        res = x

print(res)
