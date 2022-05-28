#그리디는 정렬 
#회의가 끝나는 시간으로 정렬
n = int(input())
meeting = []
for i in range(n):
    s,e = map(int,input().split())
    meeting.append((s,e)) #튜플 형식

meeting.sort(key=lambda x : (x[1],x[0]))

et = 0
cnt = 0
for s,e in meeting:
    if s >=et:
        et = e
        cnt +=1

print(cnt)
