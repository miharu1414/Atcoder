n,d = map(int,input().split())
lr = [map(int,input().split()) for i in range(n)]
l,r = [list(i) for i in zip(*lr)]

lr = []
for i in range(n):
    lr.append([l[i],r[i]])
lr.sort()

i = 0
destroyed = 0
pos = 0
ans = 0
while i< n:
    if pos == 0:
        start = r[i]-1
        i+=1
        destroyed += 1
        ans += 1
        pos = 1
    elif pos == 1:
        if l[i] <= start + d:
            destroyed += 1
            i+=1
        elif l[i] <= start:
            start = r[i] - 1
            destroyed += 1
            i+=1
        else:
            pos = 0

print(ans)
            
    