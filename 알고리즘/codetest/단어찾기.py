dict = {}
n = int(input())
for i in range((n)):
    word=input()
    dict[word]=1

for i in range((n-1)):
    word=input()
    dict[word]=0

for key, val in dict.items():
    if val==1:
        print(key)
        break
