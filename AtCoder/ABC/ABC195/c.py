n = int(input())

kijun = str(n)

keta = [0]*(17)
for i in range(1,16):


    keta[i]= (10**i-10**(i-1))*((i-1)//3)

ke = len(str(n))

ans = 0
for i in range(0,ke):
    ans += keta[i]

pura = (ke-1)//3
ans = ans+ (n-10**int(ke-1)+1)*pura
print(int(ans))