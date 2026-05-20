class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips,key=lambda t: t[1])
        min_heap = [] # [endTime, numPass]
        curr_cap = 0

        for t in trips:
            num_pass, start, end = t

            # finding out if we dropped out passengers
            while min_heap and min_heap[0][0] <=start :
                endTime, numPass = heapq.heappop(min_heap)
                curr_cap-=numPass
            
            # adding passengers
            curr_cap+=num_pass

            # checking capacity
            if curr_cap>capacity:
                return False
            heapq.heappush(min_heap, [end,num_pass])
        return True