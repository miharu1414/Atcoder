n = int(input())
s = input()
q = int(input())
tab = [map(int,input().split()) for i in range(q)]
t, a, b = [list(i) for i in zip(*tab)]

String_idx = []*(2*n)
for_s = []
back_s = []
for i in range(n):
    for_s.append(s[i])
    back_s.append(s[n+i])


is_rev = 0
for i in range(q):
    a[i] -= 1
    b[i] -= 1
    if t[i] == 1:
        if is_rev:
            
            if a[i] >= n:
                if b[i] >= n:
                    c = for_s[a[i]-n]
                    for_s[a[i] - n] = for_s[b[i]-n]
                    for_s[b[i] - n] = c 
                else:
                    c = for_s[a[i]-n]
                    for_s[a[i] - n] = back_s[b[i]]
                    back_s[b[i]] = c 
                    
            else:
                if b[i] >= n:

                    c = back_s[a[i]]
                    back_s[a[i]] = for_s[b[i]-n]
                    for_s[b[i] - n] = c 
                else:
                    c = back_s[a[i]]
                    back_s[a[i]] = back_s[b[i]]
                    back_s[b[i]] = c 
                
        else:
            if a[i] >= n:
                if b[i] >= n:

                    c = back_s[a[i]-n]
                    back_s[a[i] - n] = back_s[b[i]-n]
                    back_s[b[i] - n] = c 
                else:
                    c = back_s[a[i] - n]
                    back_s[a[i] - n] = for_s[b[i]]
                    for_s[b[i]] = c 
                
                    
            else:
                if b[i] >= n:
                    c = for_s[a[i]]
                    for_s[a[i]] = back_s[b[i]-n]
                    back_s[b[i]-n] = c 
                    
                else:
                    c = for_s[a[i]]
                    for_s[a[i] - n] = for_s[b[i]]
                    for_s[b[i] - n] = c 
            
        
    
    else:
        is_rev ^= 1

ans = ''
if not is_rev:
    ans = ''.join(for_s + back_s)

else:
    ans = ''.join(back_s + for_s)

print(ans)