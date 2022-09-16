h, w = map(int,input().split())
a = [ list(map(int,input().split())) for i in range(h)]
b = [ list(map(int,input().split())) for i in range(h)]


Dx = [0,1,0,1]
Dy = [0,0,1,1]

def cal(hairetu,i,j):
    count = 0
    for dx,dy in zip(Dx,Dy):
        count+= hairetu[i+dx][j+dy]
    return count

def sub(hairetu,i,j,a):
    for dx,dy in zip(Dx,Dy):
        hairetu[i+dx][j+dy] -= a

ans = 0



for i in range(h-1):
    for j in range(w-1):
        weight = b[i][j] 
        dif = weight - a[i][j]
        ans += abs(dif)

        sub(b,i,j,dif)


if a == b:
    print("Yes")
    print(ans)
    exit()
print("No")