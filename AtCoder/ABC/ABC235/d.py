import sys
sys.setrecursionlimit(10 ** 6)

a,n = map(int,input().split())


Ans = []

mita = set()
def rec(x,ans):
    if x in mita:
        return False
    mita.add(x)



    def Min(X):
        leg = len(str(X))
        st = str(X)

        lis =[]

        for i in range(leg):
            lis.append(st[i])
        lis.sort(reverse=True)
        A = 0
        for i in range(leg):
            A += int(lis[i])*10**i
        return A
    if x == n:
        Ans.append(ans)
        return True
    if len(str(Min(x)))>len(str(n)):
        return False

    
    rec(x*a,ans+1)
    if x%10 != 0 and x//10 != 0:
        length = len(str(x))
        rec(x//10+(x%10)*10**(length-1),ans+1)
        


rec(1,0)
if len(Ans) == 0:
    print(-1)
else:
    print(min(Ans))
