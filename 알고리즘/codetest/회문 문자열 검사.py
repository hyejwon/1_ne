#회문 문자열 검사
n = int(input())
for i in range(n):
    s = input()
    s = s.lower()
    if s[::-1]==s:
        print(f'#{i+1}','YES')
    else:
        print(f'#{i+1}','NO')