n,c = map(int,input().split())
bit = [[0,1] for i in range(31)]

for i in range(n):
    t,a = map(int,input().split())
    for i in range(31):
        x = a>>i & 1
        if t == 1:
            bit[i][0] &= x
            bit[i][1] &= x
    
        elif t == 2:
            bit[i][0] |= x
            bit[i][1] |= x
        else:
            bit[i][0] ^= x
            bit[i][1] ^= x
        
    nc = c
    ans = 0
    for i in range(31):
        ans |= (bit[i][nc>>i & 1]<<i)
    c = ans
    print(ans)