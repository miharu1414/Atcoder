n = int(input())
s = input()

def stoi(x,i):
    if ord(x) + i > ord('Z'):
        return chr(ord(x) + i-ord('Z')+ord("A")-1)
        
    return chr(ord(x)+i)

ans = ''
for S in s:
    ans += stoi(S,n)
print(ans)