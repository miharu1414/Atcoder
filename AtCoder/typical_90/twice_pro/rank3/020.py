a,b,c = map(int,input().split())
i = 1
C = c
while i<b:
    c*= C
    i+=1
    if a< c:
        print("Yes")
        exit()

print("No")