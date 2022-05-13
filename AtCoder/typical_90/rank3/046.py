n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
a_mod = [0]*46
b_mod = [0]*46
c_mod = [0]*46

for i in range(n):
    a_mod[a[i]%46]+=1
    b_mod[b[i]%46]+=1
    c_mod[c[i]%46]+=1

ans = 0

for i in range(46):
    numa = a_mod[i]
    for j in range(46):
        numb = b_mod[j]
        cnum = c_mod[(46-i-j)%46]
        if cnum>0:
            ans += numa*numb*cnum

print(ans)