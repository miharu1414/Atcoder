n = int(input())
a = list(map(int,input().split()))
a.sort(reverse = True)
ans = []
for i in range(3):
    ans.append(a[i])

A = []
arr = [0, 1, 2]
import itertools
for v in list(itertools.permutations(arr)):
    couho = ''
    for i in v:
        couho += str(ans[i])
    A.append(couho)
A.sort(reverse=True)
print(A[0])