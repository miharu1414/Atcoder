import re


n,x,y,z = map(int,input().split())
a  = list(map(int,input().split()))
b = list(map(int,input().split()))

suugaku = []
for i in range(n):
    suugaku.append([a[i],-i])

suugaku.sort(reverse=True)

pas = set()
for i in range(x):
    pas.add(-suugaku[i][1])
eigo = []
for i in range(n):
    if i not in pas:
        eigo.append([b[i],-i])
eigo.sort(reverse=True)
for i in range(y):
    pas.add(-eigo[i][1])

goukei = []
for i in range(n):
    if i not in pas:
        goukei.append([b[i]+a[i],-i])
goukei.sort(reverse=True)

for i in range(z):
    pas.add(-goukei[i][1])
ans = []
for i in range(n):
    if i in pas:
        ans.append(i+1)
for i in range(len(ans)):
    print(ans[i])
