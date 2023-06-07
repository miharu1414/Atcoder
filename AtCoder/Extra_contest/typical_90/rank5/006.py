import heapq
n, k = map(int,input().split())
s = input()

# 長さNの文字列のうち、長さがKの部分文字列を作るためには、左からN-K-i個の中からi個を必ず選ばないといけない。
sub_s = ""
heap = []
now = -1
for i in range(n):
    if i < n-k:
        heapq.heappush(heap,[s[i],i])
        continue
    heapq.heappush(heap,[s[i],i])
    nok = 1
    while nok:
        next_s, idx = heapq.heappop(heap)
        if now < idx:
            nok = 0
            now = idx
            sub_s = sub_s + next_s
            
print(sub_s)
        