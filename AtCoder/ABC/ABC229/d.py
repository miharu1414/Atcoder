s = input()
k = int(input())

r,l = 0,0
amari = k
ans = 0
while r <len(s):
    if amari > 0:
        if s[r] == ".":
            amari -= 1
        r+=1
    elif r < len(s) and s[r] == 'X':
        r += 1
    else:                                      
        if s[l] == '.':
            amari += 1
        l += 1
    ans = max(ans,r-l)
print(ans)