"""
전역변수와 지역변수
함수는 지역변수가 우선이다.
"""

def DFS1():
    cnt = 3 #DFS1의 로컬변수
    print(cnt)

def DFS2():
    global cnt #cnt 는 전역 변수 선언
    if cnt == 5: #전역변수로써 작동 함 
        cnt = cnt + 1 
        print(cnt)

if __name__ == "__main__":
    cnt = 5 #전역변수는 모든 함수가 접근 가능
    DFS1()
    DFS2()
    print(cnt)