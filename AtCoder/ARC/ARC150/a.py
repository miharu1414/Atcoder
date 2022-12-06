t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    s = input()
    s = '0' + s + '0'
    
    l,r = 0,len(s)-1
    cnt = 0
    for j in range(len(s)):
        if s[j] == '1':
            cnt+=1
    
    if cnt==0:
        hatena = dict()
        hatena[k+1]=0
        hatena[k]=0
        num = 0
        for j in range(len(s)):
            if s[j] == '?':
                num += 1
            else:
                if min(num,k+1) in hatena:
                    hatena[min(num,k+1)]+=1
                else:
                    hatena[min(num,k+1)] = 1
                num = 0
        if min(num,k+1) in hatena:
            hatena[min(num,k+1)]+=1
        else:
            hatena[min(num,k+1)] = 1
        if hatena[k+1]>0 or hatena[k]!=1:
            print("No")
        else:
            print("Yes")
        continue
    
    for j in range(len(s)):
        if s[j] == '1':
            l = j
            break

    for j in range(len(s)-1,-1,-1):
        if s[j] == '1':
            r = j
            break
    cnt0 = 0
    for j in range(l,r+1):
        if s[j] == '0':
            cnt0+=1
    if cnt0:
        print("No")
        continue
    ans1 = r - l + 1
    if ans1 == k:
        print("Yes")
        continue
    if s[l-1] == '?' and s[r+1]=='?':
        
        for j in range(l-1,-1,-1):
            if s[j]=='0':
                break
            if s[j]=='?':
                ans1+=1
        for j in range(r+1,len(s),1):
            if s[j]=='0':
                break
            if s[j]=='?':
                ans1+=1
        if ans1 == k:
            print("Yes")
            continue
        print("No")
    else:
        ans2 = ans1
        for j in range(l-1,-1,-1):
            if s[j]=='0':
                break
            if s[j]=='?':
                ans2+=1
        for j in range(r+1,len(s),1):
            if s[j]=='0':
                break
            if s[j]=='?':
                ans2+=1
        if ans1<=k<=ans2:
            print("Yes")
        else:
            print("No")
        
                