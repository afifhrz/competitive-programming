import bisect
from collections import defaultdict

N, L, R = map(int, input().split())
S = input()

pos = defaultdict(list)
ans = 0

for j in range(N):
    c = S[j]
    
    left = j - R
    right = j - L
    
    if right >= 0:
        # clamp left bound
        left = max(left, 0)
        
        lst = pos[c]
        
        # count indices in [left, right]
        l = bisect.bisect_left(lst, left)
        r = bisect.bisect_right(lst, right)
        
        ans += (r - l)
    
    pos[c].append(j)

print(ans)