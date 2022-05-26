#자릿수의 합
t =  int(input())
a = list(map(int,input().split()))
def digit_sum(x):
    x = list(str(x))
    s= 0
    for i in x:
        s+=int(i)
    return s,i

for i in range(t):
    max = digit_sum(a[0])
    if max<digit_sum(a[i]):
        max = digit_sum(a[i])
    print(a[i])
