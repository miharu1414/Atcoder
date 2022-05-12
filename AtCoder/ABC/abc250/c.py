n,q = map(int,input().split())
x = [int(input()) for i in range(q)]
pos = [i for i in range(n)]
num = [i for i in range(n)]
for i in range(n):
    pos[i] = i
for i in range(q):
    x[i] -= 1
for i in range(q):
    if pos[x[i]] == n-1:
        sub = pos[x[i]]
        sub2 = num[pos[x[i]]-1]

        pos[x[i]] -=1 
        
        num[pos[x[i]]] = x[i]
        pos[sub2] +=1 
        num[sub] = sub2

        
    else:
        sub = pos[x[i]]
        sub2 = num[pos[x[i]]+1]

        pos[x[i]] +=1 
        
        num[pos[x[i]]] = x[i]
        pos[sub2] -=1 
        num[sub] = sub2
for i in range(n):
    num[i] +=1

print(*num)