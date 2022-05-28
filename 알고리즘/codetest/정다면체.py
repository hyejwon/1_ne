#정다면체
<<<<<<< HEAD
n,m = map(int,input().split())
cnt=[0]*(n+m+3) #합의 개수를 세는 리스트를 생성
for i in range(1,n+1):
    for j in range(1,m+1):
        cnt[i+j]+=1
max = -2147000000
for i in range(n+m+1):
    if cnt[i]>max:
        max = cnt[i]

for i in range(n+m+1):
    if cnt[i] == max:
        print(i,end=' ')

=======
# n면체와 m면체의 두 개의 주사위 눈의 합 중 가장 확률이 높은 숫자 출력
n,m = map(int,input().split())
cnt = [0]*(n+m+3)
max=0
for i in range(1,n+1):
    for j in range(1,m+1):
        cnt[i+j] +=1 #cnt를 두 눈의 합의 빈도수로 지정 

for i in range(n+m+1):
    if cnt[i] > max :
        max=cnt[i]  #최댓값 설정하기. 이때 max 초기값 설정


for i in range(n+m+1):
    if cnt[i] == max:
        print(i , end=' ')#최대 카운트 수에 해당하는 인덱스들 출력
>>>>>>> ce4acdac3232f62df47e27cc43a43549775cf19c

