n, w = map(int,input().split())
stp = [map(int,input().split()) for i in range(n)]
s,t,p = [list(i) for i in zip(*stp)]

arr = []
for i in range(n):
    arr.append([s[i],p[i]])
    arr.append([t[i],-p[i]])

arr.sort()

necessary = dict()
now = 0
for time,W in arr:
    now += W
    necessary[time] = now

for k,W in necessary.items(): 
    if W > w:
        print("No")
        exit()
print("Yes")
    
