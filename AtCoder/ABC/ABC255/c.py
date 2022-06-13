x,a,d,n = map(int,input().split())
if d==0:
    print(abs(x-a))
    exit()
if d>0:
    if (x-a)/d >= n-1:
        print(x-a-d*(n-1))
        exit()
    if x<=a:
        print(a-x)
        exit()
    I = (x-a)//d
    low = abs(x - a -d*I)
    up =   abs(x - a -d*(I+1))
    print(min(low,up))
else:
    if (x-a)/d >= n-1:
        print(abs(x-a-d*(n-1)))
        exit()
    if x>=a:
        print(abs(x-a))
        exit()
    I = (x-a)//d
    low = abs(x - a -d*I)
    up =   abs(x - a -d*(I+1))
    print(min(low,up))