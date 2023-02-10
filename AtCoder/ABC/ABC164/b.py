a,b,c,d = map(int,input().split())

while a > 0 and c > 0:
    c -= b
    if c <= 0:break
    
    a -= d
    if a<= 0:break

if c <= 0:
    print("Yes")
else:
    print("No")