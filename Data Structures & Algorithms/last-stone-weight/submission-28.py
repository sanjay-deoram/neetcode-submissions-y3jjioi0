class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Conver to max heap
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        if len(maxHeap)==1:
            return -maxHeap[0]
            
        while len(maxHeap)>1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)

            if x!=y:
                print(x,y)
                res = abs(x-y)
                heapq.heappush(maxHeap,-res)
        return -maxHeap[0] if maxHeap else 0