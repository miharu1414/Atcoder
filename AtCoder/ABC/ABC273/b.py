x,k = map(int,input().split())
from decimal import Decimal, getcontext, ROUND_HALF_UP
ans = x
c = getcontext()  # 現在の演算コンテキストを取得
c.rounding = ROUND_HALF_UP  # 丸めモードとして四捨五入を指定
d = Decimal(str(x))
for i in range(k):
    ans = d.quantize(Decimal(str('1e1')), rounding=ROUND_HALF_UP)
    ans = ans//10
    d = Decimal(str(ans))
print(ans*10**k)