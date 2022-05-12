

N, q = map(int,input().split())
a = list(map(int,input().split()))
t = []
x = []
y = []
shift = 0
for i in range(q):
    T,X,Y = map(int,input().split())
    X-=1
    Y-=1
    t.append(T)
    x.append(X)
    y.append(Y)
    shift1 = shift
    shift2 = shift

    if X - shift1<0:
        shift1 -= X
        shift1 %= N
        X = N-shift1

    if Y - shift2 <0:
        shift2 -= Y
        shift2 %= N
        Y = N-shift2

    if T == 1:
    

        sub = a[X]
        a[X] = a[Y] 
        a[Y] = sub
        
    elif T==2:
        shift+=1

    else:
        print(a[X])
