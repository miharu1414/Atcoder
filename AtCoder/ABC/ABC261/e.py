n,c = map(int,input().split())
bit = [[0,1] for i in range(30)]

for i in range(n):
    t,a = map(int,input().split())
    for j in range(30):
        x = a >> j & 1
        if t == 1:
            bit[j][0] &= x
            bit[j][1] &= x
        elif t == 2:
            bit[j][0] |= x
            bit[j][1] |= x
        else:
            bit[j][0] ^= x
            bit[j][1] ^= x
        
    nc = 0
    for j in range(30):
        if bit[j][c>>j&1]:
            nc |= 1 <<j
    c = nc

    print(c) 