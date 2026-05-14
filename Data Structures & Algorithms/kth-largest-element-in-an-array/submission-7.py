class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # minheap
        minHeap = []

        for num in nums:
            heapq.heappush(minHeap, num)
            # keeps size of k
            if len(minHeap)>k:
                heapq.heappop(minHeap)
        return minHeap[0]