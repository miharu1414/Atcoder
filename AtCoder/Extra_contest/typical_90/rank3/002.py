n = int(input())
if n %2 == 1:
    exit(0)
kakko = []
from itertools import product
right = 0
left= 0
ans = []
def judge(pro,ans):
    right = 0
    left= 0
    for i in range(n):
        if pro[i]:
            right +=1
        elif pro[i]==0 and left<right:
            left +=1
        else:
            return 0
    
    if right == left:
        s=''
        for i in range(n):
            if pro[i]==1:
                s += '('
            else:
                s += ')'
        ans.append(s)

for kakko in product([0, 1], repeat=n):
    judge(kakko,ans)
ans.sort()
for s in ans:
    print(s)