cnt = 0
a = int(input())

while a >=0:
    if a % 5 == 0 :
        a = a//5
        cnt += a
        print(cnt)
        break
    a -=3
    cnt +=1

else:
    print(-1)    