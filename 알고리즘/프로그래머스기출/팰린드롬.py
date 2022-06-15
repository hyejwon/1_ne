#가장 긴 팰린드롬 판별 - 프로그래머스

def ispalindrome(x):
    if x==x[::-1]:
        return True

def palindrome(s):
    max=0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if ispalindrome(s[i:j]):
                if max<len(s[i:j]):
                    max = len(s[i:j])
    return max

s = str(input())
result = palindrome(s)
print(result)



