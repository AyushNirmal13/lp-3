import heapq

n = int(input())
heap = [[int(f), [c, ""]] for c, f in (input().split() for _ in range(n))]
heapq.heapify(heap)

while len(heap) > 1:
    a, b = heapq.heappop(heap), heapq.heappop(heap)
    for pair in a[1:]: pair[1] = '0' + pair[1]
    for pair in b[1:]: pair[1] = '1' + pair[1]
    heapq.heappush(heap, [a[0] + b[0]] + a[1:] + b[1:])

for ch, code in sorted(heap[0][1:]):
    print(f"{ch} : {code or '0'}")
