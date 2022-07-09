n = int(input())
a = []
s = []
for i in range(n):
    x = input()
    s.append(x)
    A =[]
    for j in x:
        A.append(int(j))
    a.append(A)

X = []
for i in range(n):
    b = []
    for j in range(n):
        b.append(s[i][j])
    X.append(b)
    b =[]
    for j in range(n-1,-1,-1):
        b.append(s[i][j])
    X.append(b)

    b = []
    for j in range(n):
        b.append(s[j][i])
    X.append(b)

    b =[]
    for j in range(n-1,-1,-1):
        b.append(s[j][i])
    X.append(b)
    b = []
    for j in range(n):
        b.append(s[(i+j)%n][j])
    X.append(b)

    b = []
    for j in range(n):
        b.append(s[(i-j)%n][j])
    X.append(b)

    b = []
    for j in range(n-1,-1,-1):
        b.append(s[(i-j)%n][j])
    X.append(b)

    b = []
    for j in range(n-1,-1,-1):
        b.append(s[(i+j)%n][j])
    X.append(b)

def max_x(x):
    ans = []
    for i in range(len(x)):
        b = []
        for j in range(len(x)):
            B = int(x[(i+j)%len(x)])
            b.append(B)
        ans.append(b)
    ans.sort(reverse=True)
    return ans[0]

A= []
for i in X:
    AS = max_x(i)
    A.append(AS)
A.sort(reverse = True)
s = ""
for i in range(len(A[0])):
    s += str(A[0][i])
print(s)
