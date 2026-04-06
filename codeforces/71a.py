n = int(input())
words = []
for _ in range(n):
    words.append(input())

for item in words:
    if len(item) > 10:
        print(item[0]+str(len(item[1:-1]))+item[-1])
    else:
        print(item)