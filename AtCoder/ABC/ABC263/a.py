a = list(map(int,input().split()))
import collections

c = collections.Counter(a)
d = c.most_common()
if len(d) == 2 and d[0][1] == 3 and d[1][1] ==2:
    print("Yes")
else:
    print("No")