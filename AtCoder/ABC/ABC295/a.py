n = int(input())
q = map(str, input().split())
words = ["and", "not", "that", "the", "you"]
for w in q:
    if w in words:
        print("Yes")
        exit()
print("No")
