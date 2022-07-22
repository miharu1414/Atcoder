n = int(input("ノード数:"))
G =[[0]*(n+1) for i in range(n+1)]


print("例:aからbへの辺 a -> b")
while True:

    a,b = map(int,input().split())
    if a*b == 0:
        break
    G[a][b] = 1
    G[b][a] = -1
    for i in range(1,n+1):
        if G[i][a] == 1:
            G[b][i] = -1
            G[i][b] = 1
G[n][n] = -1

print(f'   ',end = '')
for i in range(1,n+1):
    print(' %2d ' %i,end ='')
print()
for i in range(1,n+1):
    print('%2d:' %i,end = '')
    for j in range(1,n+1):
        if G[i][j] == 0:
            print('    ', end='')
        elif G[i][j] == 1:
            print(' +1 ', end='')
        else:
            print(' -1 ', end='')
    print()
