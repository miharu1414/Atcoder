n,k,p =map(int,input().split())
s = input()

solve = [[0,0] for i in range(k+1)]
for i in range(k):
    if i < n:
        if s[i]=='A':
            if  p > 50:
                solve[i+1][0] = solve[i][0]+1
                solve[i+1][1] = solve[i][1]
            elif p == 50:
                solve[i+1][0] = solve[i][0]
                solve[i+1][1] = solve[i][1]
            else:
                solve[i+1][0] = solve[i][0]
                solve[i+1][1] = solve[i][1] + 1
        else:
            if  p < 50:
                solve[i+1][0] = solve[i][0]+1
                solve[i+1][1] = solve[i][1]
            elif p == 50:
                solve[i+1][0] = solve[i][0]
                solve[i+1][1] = solve[i][1]
            else:
                solve[i+1][0] = solve[i][0]
                solve[i+1][1] = solve[i][1] + 1
    else:
        solve[i+1][0] = solve[i][0]
        solve[i+1][1] = solve[i][1]

ans = ''
for i in range(1,k+1):
    if solve[i][0] > solve[i][1]:
        ans += '+'
    elif solve[i][0]  == solve[i][1]:
        ans += '0'
    else:
        ans += '-'
        
print(ans)
            