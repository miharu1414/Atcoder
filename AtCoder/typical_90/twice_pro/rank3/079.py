h,w = map(int,input().split())
a = [list(map(int,input().split())) for i in range(h)]
b = [list(map(int,input().split())) for i in range(h)]

def dif(A,B,i,j):
    diffe = abs(A[i][j]-B[i][j])
    if A[i][j] >= B[i][j]:
        B[i][j] += diffe
        B[i+1][j] += diffe
        B[i][j+1] += diffe
        B[i+1][j+1] += diffe
    else:
        B[i][j] -= diffe
        B[i+1][j] -= diffe
        B[i][j+1] -= diffe
        B[i+1][j+1] -= diffe    
    return diffe

ans = 0
for i in range(h-1):
    for j in range(w-1):
        ans +=dif(a,b,i,j)
    
if a == b:
    print("Yes")
    print(ans)
else:
    print("No")