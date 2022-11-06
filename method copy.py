time = [int(input()) for i in range(10)]
gyouretu = [list(map(int,input().split())) for i in range(10)]

ans = [0]*10

for i in range(10):
    ans[i] = time[i]
    for j in range(10):
        ans[i] += max(gyouretu[i][j],0)*time[j]
for i in range(10):
    print(f'{i+1}:{ans[i]}')