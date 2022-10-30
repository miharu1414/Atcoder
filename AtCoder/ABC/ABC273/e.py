q = int(input())

a = []
book = dict()
now = 0

book[0] = []
for i in range(q):
    que = input()
    if 'ADD' in que:
        _,x = que.split()
        x = int(x)
        
        
        book[now].append(x)
        
    elif 'SAVE' in que:
        _,x = que.split()
        x = int(x)
        book[x] = book[now]
        
    elif 'LOAD' in que:
        _,x = que.split()
        x = int(x)
        now = x
        if now not in book:
            book[now] = []
    else:
        if len(a)!=0:
            a.pop()
    
    if len(book[now]) == 0:
        print('-1',end=' ')
    else:
        print(book[now][-1],end=' ')
        
    