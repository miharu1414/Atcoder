s = input()
A = [0]*(len(s)+1)
mod = 2019
mod_n = [0]*2019
mod_n[0] = 1
for i in range(len(s)):
    now = len(s) - i - 1
    A[i+1] = ((pow(10,i,mod) * int(s[now]))%mod + A[i])%mod
    mod_n[A[i+1]]+=1
ans = 0 
for i in range(2019):
    ans += (mod_n[i]* (mod_n[i]-1))//2
print(ans)
    

    