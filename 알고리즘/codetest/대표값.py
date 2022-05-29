n = int(input())
a = list(map(int,input().split()))
avr=sum(a)/len(a)
avr=avr+0.5 #round는 round_half_even
avr=int(avr)
min=2147000000
for idx, x in enumerate(a):
    tmp=abs(x-avr)
    if tmp <min:
        min = tmp
        score=x
        res = idx+1
    elif tmp == min:#답이 두개
        if x > score: #>=인경우 문제에 맞지 않게 뒤 번호가 출력됨
            score = x
            res = idx +1
print(avr,res)