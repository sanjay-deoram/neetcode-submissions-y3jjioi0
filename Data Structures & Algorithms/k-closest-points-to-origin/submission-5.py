class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        initial thoughts: tuple (dist,x,y) 
        we min heapify by dist using min heap.
        pop until k
        """
        minHeap = []
        for point in points:
            x = (point[0] - 0)**2
            y = (point[1] - 0)**2
            dist = math.sqrt(x + y)
            heapq.heappush(minHeap,(dist,point[0],point[1]))
        res = []
        for i in range(0,k):
            num = heapq.heappop(minHeap)
            res.append([num[1],num[2]])
        return res
