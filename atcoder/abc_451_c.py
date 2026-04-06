import heapq


Q = int(input())
heap = []
count = 0

for _ in range(Q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        h = query[1]
        heapq.heappush(heap, h)
        count += 1
    
    else:
        h = query[1]
        while heap and heap[0] <= h:
            heapq.heappop(heap)
            count -= 1
    
    print(count)