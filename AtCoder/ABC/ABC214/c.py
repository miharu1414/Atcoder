n = int(input())
s = list(map(int,input().split()))
t = list(map(int,input().split()))
mint = 1000000000
nummint = 
for i in range(n):
    if mint>t[i]:
        nummint = i
        mint = t[i]

for i in range()