n,q = map(int,input().split())
s = input()

start = 0

for i in range(q):
    t,x = map(int,input().split())
    if t == 1:
        start += x
    
    else:
        now = n-start%n

        print(s[(now+x-1)%n])
