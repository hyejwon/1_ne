def reverse(x):
    s = str(x)
    s = s[::-1]
    if s.startswith('0'):
        s = s.replace('0',"")
    return s
#print(reverse(n))

#소수 판별 
def isprime(s):
    if x ==1:
        return False
    
    s = int(s)
    for j in range(2,s//2+1):#절반까지 돔 
        if s % j == 0:
            return False
    else:
        return True

n = int(input())
a = list(map(int,input().split()))

for x in a:
    s = reverse(x)
    if isprime(s):
        print(s,end=' ')
