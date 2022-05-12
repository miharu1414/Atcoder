h,w = map(int,input().split())
r,c = map(int,input().split())
ans = 4
if h==1 or w==1:
    ans = 3
if h==1 and w==1:
    ans =2
if r == 1 or r==h:
    ans -=1 
if c == 1 or c == w:
    ans-=1
print(ans)