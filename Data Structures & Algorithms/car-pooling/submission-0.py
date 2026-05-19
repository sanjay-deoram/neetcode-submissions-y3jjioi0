class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key=lambda t: t[1])
        min_heap = [] # [endTime, numPass]
        curr_capacity = 0

        for t in trips:
            cap, start, end = t
            
            while min_heap and min_heap[0][0] <= start:
                end_time, num_pass = heapq.heappop(min_heap)
                curr_capacity -= num_pass

            curr_capacity += cap
            if curr_capacity > capacity:
                return False
            heapq.heappush(min_heap, [end, cap])
        return True