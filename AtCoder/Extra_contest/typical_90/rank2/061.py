q = int(input())
t =[]
x = []
for i in range(q):
    a,b = map(int,input().split())
    t.append(a)
    x.append(b)

que = [0]*200001
up = 100001
down = 100000
for i in range(q):

    if t[i] ==1:
        que[up] = x[i]
        up+=1
    elif t[i]==2:
        que[down] = x[i]
        down-=1

    else:
        print(que[up-x[i]])
    