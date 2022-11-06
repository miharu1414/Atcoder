n = int(input())

num = []
for i in range(len(str(n))):
    num.append(int(str(n)[i]))
num.sort(reverse=True)
ans = 0
for i in range(2 ** len(num)):
    bag1 = []
    bag2 = []

    for j in range(len(num)):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            bag1.append(num[j])  # フラグが立っていたら bag に果物を詰める
        else:
            bag2.append(num[j])
        
    if len(bag1) ==0 or len(bag2)==0:
        continue
    a1 = ''
    for i in bag1:
        a1+=str(i)
    a2 = ''
    for j in bag2:
        a2+=str(j)
    ans = max(ans,int(a1)*int(a2))
print(ans)