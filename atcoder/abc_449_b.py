h, w, q = map(int, input().split())
for _ in range(q):
    q_type, cnt = map(int, input().split())
    if q_type == 1:
        h -= cnt
        print(cnt*w)
    else:
        w -= cnt
        print(cnt*h)