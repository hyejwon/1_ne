#점수계산
#import sys 
#sys.stdin =open("/Users/wonhyejin/Documents/1_ne/알고리즘/codetest/100","rt")
n =int(input())
a = list(map(int,input().split()))
sum = 0
cnt = 0
for x in a:
    if x ==1:
        cnt+=1
        sum+=cnt
    else:
        cnt=0 
print(sum)