n, k = map(int,input().split())
s = input()

import math

def make_div(n):
    div = []
    for i in range(1,n+1):
        if n % i ==0:
            div.append(int(i))
    return div

div = make_div(n)
div.sort()


def check(i,k):
    i = int(i)
    

    ans = 0
    boolen = 0
    sum_cost = 0
    for j in range(i):
        cha = [0]*200
        for p in range(n//i):
            cha[ord(s[p*i+j])]+=1
        max_pos = 0
        for l in range(len(cha)):
            if cha[max_pos] < cha[l]:
                max_pos  = l
        cha[max_pos] = 0
        cost = sum(cha)

        sum_cost += cost

    if sum_cost <= k:
        return 1
    else:
        return 0


    
        
answer = n
for i in div:
    if check(i,k) ==1:
        print(i)
        exit()
print(answer)