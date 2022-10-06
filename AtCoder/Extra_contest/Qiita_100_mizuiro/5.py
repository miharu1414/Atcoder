n = int(input())
a = list(map(int,input().split()))
q = int(input())
m = list(map(int,input().split()))

possible = dict()
for i in range(2 ** n):
    num = 0
    
    for j in range(n):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            num += a[j]
    possible[num] = 1

for Q in m:
    if Q in possible:
        print("yes")
    else:
        print("no")
