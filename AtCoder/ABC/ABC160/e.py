x,y,a,b,c = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
r = list(map(int,input().split()))
p.sort(reverse=True)
q.sort(reverse=True)

ans = p[:x] + q[:y] + r
ans.sort(reverse=True)
print(sum(ans[:x+y]))
