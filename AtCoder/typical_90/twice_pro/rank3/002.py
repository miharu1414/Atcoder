n = int(input())
import itertools

if n %2 ==1:
    exit()
def judge(s):
    count_l,count_r = 0,0
    i = 0
    while 1:
        if s[i] == 0:
            count_l+=1
        else:
            count_r += 1
        if count_l < count_r:
            return 0
        i+=1
        if i == n:
            if count_l == count_r:
                return 1
            else:
                return 0
def shift(s):
    S = ""
    for i in range(n):
        if s[i] == 0:
            S += '('
        else:
            S += ')'
    return S


A = itertools.product([0,1], repeat=n)

ans = []
for l in A:

    if judge(l):
        ans.append(shift(l))
ans.sort()
for s in ans:
    print(s)