n, k = map(int,input().split())
p = [list(map(int,input().split())) for i in range(n)]

num = [0]*n
for i in range(n):
    for j in range(3):
        num[i] += p[i][j]

kouho = []
for i in range(n):
    kouho.append([num[i],i])
kouho.sort(reverse=True)

ans = [0]*n


tensuu  = kouho[k-1][0]

for i in range(n):
    if num[i] + 300 >= tensuu:
        print("Yes")
    else:
        print("No")