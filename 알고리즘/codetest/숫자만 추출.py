#숫자만 추출
import re
s = input() 
numbers = re.sub(r'[^0-9]','', s)
if numbers.startswith('0'):
    n=int(numbers)
#n=int(numbers)
print(n)

cnt = 2 #1과 자기 자신 
for i in range(2,n//2+1):
    if n % i ==0:
        cnt +=1
print(cnt)


for x in s:
    if x.isdecimal(): # 0부터 9까지 숫자인지
        res=res*10+int(x)
