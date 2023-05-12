n = int(input())

s = [-1]*(n+1)
s[1] = 0
s[n] = 1
mid = n//2
left = 0
right = n+1
for i in range(20):
    print(f'? {mid}')
    ans = int(input())
    s[mid] = ans
    if mid>1 and  s[mid] != s[mid-1] and s[mid-1] != -1:
        print(f'! {mid-1}')
        exit()
    if mid>1 and  s[mid] != s[mid+1] and s[mid+1] != -1:
        print(f'! {mid}')
        exit()
    if mid==n-1 and s[mid] != s[mid+1]:
        print(f'! {mid}')
        exit()
    if ans == 1:
        copy = mid
        mid = (mid + left)//2
        right = copy
    else:
        copy = mid
        mid = (mid + right)//2
        left = copy
    
    