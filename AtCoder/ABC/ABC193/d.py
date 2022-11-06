k = int(input())
s = input()
t = input()

num = [k]*(10)
aoki = [0]*10
takahashi = [0]*(10)
for i in range(len(s)-1):
    num[int(s[i])]-=1
    num[int(t[i])]-=1
    aoki[int(t[i])]+=1
    takahashi[int(s[i])]+= 1

sousuu = (9*k - 8)*(9*k-9)

nu = 0

for i in range(1,10):
    if num[i]==0:
        continue
    num[i]-=1
    takahashi[i]+=1
    score1 = 0
    for k in range(9):
        score1 += (k+1)*10**takahashi[k+1]
        
    for j in range(1,10):
        if num[j]==0:
            continue
        aoki[j]+=1
        score2 = 0
        for k in range(9):
            score2 += (k+1)*10**aoki[k+1]
        if score1 > score2:
            nu += (num[i]+1)*(num[j])
            
        aoki[j]-=1
    num[i]+=1
    takahashi[i]-=1
print(nu/sousuu)