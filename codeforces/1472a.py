tc = int(input())
for _ in range(tc):
    w, h, n = map(int, input().split())
    count = 1
    if w % 2 != 0 and h % 2 != 0:
        if count >= n:
            ans = "YES"
        else:
            ans = "NO"
    else:
        while w % 2 == 0:
            w //= 2
            count *= 2
        while h % 2 == 0:
            h //= 2
            count *= 2
        if count >= n:
            ans = "YES"
        else:
            ans = "NO"
    print(ans)