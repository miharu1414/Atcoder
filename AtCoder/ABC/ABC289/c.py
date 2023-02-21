n, m = map(int,input().split())
a = []
C = []
for i in range(m):
    c = int(input())
    C.append(c)
    A = list(map(int,input().split()))
    a.append(A)

cnt = 0
for i in range(2 ** m):
    bag = []
    ans = [0]*n
    for j in range(m):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            for k in range(C[j]):
                ans[a[j][k]-1] = 1
    if sum(ans) == n:
        cnt += 1
print(cnt)