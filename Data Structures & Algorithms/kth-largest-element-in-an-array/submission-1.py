class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-x for x in nums]
        heapq.heapify(maxHeap)

        largest_element = float('-inf')
        for i in range(0,k):
            largest_element = heapq.heappop(maxHeap)
        return -largest_element