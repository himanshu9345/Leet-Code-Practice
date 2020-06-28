import heapq

intervals = [[100,300], [145,215], [200, 230], [215, 300], [215, 400], [400, 500], [500, 600]]
intervals.sort(key=lambda x:x[0])  # sort by start time
heap = []  # heap contains end times only
max_len, max_start, max_end = 0, 0, 0
for m in intervals:
    while heap and m[0]>=heap[0]:
        print ("ehh")
        heapq.heappop(heap)
    heapq.heappush(heap, m[1])
    if max_len<len(heap):
        max_len = len(heap)
        print (max_len,heap[0], m[0])

meetings = sorted(intervals, key=lambda k:k[1])  
heap = [(meetings[0][1], 0)]

overlaps = {}

for i in range(1, len(meetings)):
    if meetings[i][0] < heap[0][0]:
        heapq.heappush(heap, (meetings[i][1], i))
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, (meetings[i][1], i))
    
    if meetings[i][0] < heap[0][0]:
        p = (meetings[i][0], heap[0][0])
        if p in overlaps:
            overlaps[p] = max(overlaps[p], len(heap))
        else:
            overlaps[p] = len(heap)
    print (len(heap))
print( [x for x, y in overlaps.items() if y == max(overlaps.values())])