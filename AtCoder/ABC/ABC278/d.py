n = int(input())
a = list(map(int,input().split()))
sum = [0]*200001

Q = int(input())

flat = 0
last_flat = 0
rireki = []
for i in range(Q):
    qu = list(map(int,input().split()))
    if qu[0] == 1:
        flat += 1
        last_flat = qu[1]
        for k in rireki:
            sum[k] = 0
        rireki = []
        
        pass
    elif qu[0] == 2:
        rireki.append(qu[1]-1)
        sum[qu[1]-1] += qu[2]
        
    else:
        if flat == 0:
            print(a[qu[1]-1]+sum[qu[1]-1])
        else:
            print(last_flat+sum[qu[1]-1])
        