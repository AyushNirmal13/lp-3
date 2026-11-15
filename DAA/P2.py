import heapq
n = int(input("Enter number of characters: "))
if n <= 0:
    print("Invalid input")
else:
    heap = [[int(f), [c, ""]] for c, f in
            (input("Enter character and frequency: ").split() for _ in range(n))]

    heapq.heapify(heap)

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)

        for pair in a[1:]:
            pair[1] = '0' + pair[1]

        for pair in b[1:]:
            pair[1] = '1' + pair[1]

        heapq.heappush(heap, [a[0] + b[0]] + a[1:] + b[1:])

    print("\nHuffman Codes:")
    for ch, code in sorted(heap[0][1:]):
        print(f"{ch} : {code or '0'}")

# -----------------------------------------
# SAMPLE INPUT:
# 4
# A 5
# B 9
# C 12
# D 13
#
# SAMPLE OUTPUT:
# Huffman Codes:
# A : 00
# B : 01
# C : 10
# D : 11
#
# NOTE:
# Huffman Coding uses a Greedy approach.
# Lower frequency characters get shorter codes.
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)
#
# RUN:
# python P2.py
# -----------------------------------------
