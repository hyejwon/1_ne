num_cases = int(input())

cases =[]

for i in range(num_cases):
    cases.append(list(map(int, input().split())))

def_nums = {0 : [0, 1, 2, 3, 4, 5], 1 : [1, 2], 2 : [0, 1, 3, 4, 6], \
            3 : [0, 1, 2, 3, 6], 4 : [1, 2, 5, 6], 5 : [0, 2, 3, 5, 6], \
            6 : [0, 2, 3, 4, 5, 6], 7 : [0, 1, 2, 5], 8 : [0, 1, 2, 3, 4, 5, 6], \
            9 : [0, 1, 2, 3, 5, 6]}

def check(case):
    [pre, nxt] = case
    pre_comb = {0 : [], 1 : [], 2 : [], 3 : [], 4 : []}
    nxt_comb = {0 : [], 1 : [], 2 : [], 3 : [], 4 : []}
    tmp = 0
    for i in range(len(str(pre))-1, -1, -1):
        pre_comb[i].extend(def_nums[int(str(pre)[::-1][i])])
    for i in range(len(str(nxt))-1, -1, -1):
        nxt_comb[i].extend(def_nums[int(str(nxt)[::-1][i])])
    for i in range(5):
        tmp += (len(set(pre_comb[i]) - set(nxt_comb[i])) +len(set(nxt_comb[i]) - set(pre_comb[i]))) 
    return tmp

ans = []

for c in cases:
    ans.append(check(c))

for i in range(num_cases):
    print(ans[i])