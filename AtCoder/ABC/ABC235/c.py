n,q = map(int,input().split())
a = list(map(int,input().split()))

pos = [[] for i in range(2*10**5+1)]

zahyou = set()
for i in range(n):

    zahyou.add(a[i])
zahyou  = list(zahyou)

f_a = dict()
for i in range(len(zahyou)):
    f_a[zahyou[i]] = i

for i in range(n):
    pos[f_a[a[i]]].append(i)

for j in range(q):
    x,k = map(int,input().split())
    if x not in f_a:
        print(-1)
    elif k>len(pos[f_a[x]]):
        print(-1)
    else:
        print(pos[f_a[x]][k-1]+1)
