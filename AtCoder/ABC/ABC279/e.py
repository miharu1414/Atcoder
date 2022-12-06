n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(range(1, n + 1))
ss = []
for i in range(m):
    x = a[i]
    j, k = b[x - 1], b[x]
    #print(f'b={b}, x = {x}')
    ss.append((j, k))
    b[x - 1], b[x] = k, j
bx2i = {x : i for i, x in enumerate(b)}
#print(f'ss={ss}, b={b}')
ans = []
for j, k in ss:
    if j == 1:
        ans.append(bx2i[k] + 1)
    elif k == 1:
        ans.append(bx2i[j] + 1)
    else:
        ans.append(bx2i[1] + 1)
print('\n'.join(str(x) for x in ans))