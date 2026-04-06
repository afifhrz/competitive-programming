n, m = map(int, input().split())
b = {}
b_next = {}
for _ in range(n):
    b_this, b_val = map(int, input().split())
    if b_val not in b_next:
        b_next[b_val] = 1
    else:
        b_next[b_val] += 1

    if b_this not in b:
        b[b_this] = 1
    else:
        b[b_this] += 1
for i in range(1, m+1):
    print(b_next.get(i, 0) - b.get(i, 0))