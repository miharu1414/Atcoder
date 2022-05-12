from numpy import poly1d
 
# 入力
N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
 
# 多項式インスタンスの生成
polyA = poly1d(list(reversed(A)))
polyC = poly1d(list(reversed(C)))
 
# Bを求める
polyB = polyC / polyA
# Bの係数
coefB = list(map(int, polyB[0].c))
 
# 順番を逆にして出力
ans = list(reversed(coefB))
print(*ans)