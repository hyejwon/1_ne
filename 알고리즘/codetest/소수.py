#소수
ptr = 0
prime =[None]*500

prime[ptr]=2
ptr+=1

n=int(input())
for i in range(3,n+1,2):
    for j in range(1,ptr):
        if i % prime[j] ==0:
            break
    else:
        prime[ptr] = i 
        ptr+=1

print(ptr)