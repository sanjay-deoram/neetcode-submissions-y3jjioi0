class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxStones = [-x for x in stones]
        heapq.heapify(maxStones)
        
        if len(maxStones)<=1:
            return -maxStones[0]
        while len(maxStones)>1:
            print(maxStones)
            # First were pop 2 elements, x,y
            x = heapq.heappop(maxStones)
            y = heapq.heappop(maxStones)

            if x == y:
                continue
            
            res = abs(y - x)
            heapq.heappush(maxStones,-res)

        return abs(maxStones[0]) if maxStones else 0