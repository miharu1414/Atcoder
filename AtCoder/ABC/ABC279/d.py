a, b  = map(int,input().split())

def f(c):
    return  b * c + a / ((c+1)**(1/2))

x = ((a/(2*b))**2)**(1/3)
mina = 10**18
x = int(x)
for X in range(-10,10):
    ans = f(max(0,x+X))
    mina = min(mina,ans)
print(mina)