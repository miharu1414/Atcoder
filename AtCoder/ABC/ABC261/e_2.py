n,c = map(int,input().split())
f = [[0,1] for i in range(30)]

for i in range(n):
    t, a = map(int,input().split())
    for j in range(30):
        x = a>>j & 1
        if t == 1:
            f[j][0] &= x
            f[j][1] &= x
        elif t == 2:
            f[j][0] |= x
            f[j][1] |= x
        else: 
            f[j][0] ^= x
            f[j][1] ^= x
    
    nc = 0
    for j in range(30):
        if f[j][c>>j&1]:
            nc |= 1<<j
    c = nc
    print(c)
