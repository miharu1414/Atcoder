n = int(input())

k = len(str(n))
ans = k
for i in range(2 ** k):
    Sum = 0
    cnt = 0
    for j in range(k):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            Sum+=int(str(n)[j])

        else:
            cnt+=1
    if cnt == k:
        continue
    if Sum % 3== 0:
        ans = min(cnt,ans)
if ans == k:
    print(-1)
else:
    print(ans)
    