class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = [[-cnt,char] for char,cnt in count.items()]
        heapq.heapify(max_heap)
        prev = None
        res = ""
        print(max_heap)
        while max_heap or prev:
            if prev and not max_heap:
                return ""
            
            item = heapq.heappop(max_heap)
            count = item[0]
            char = item[1]
            res+=char
            # hey we used this character minus the count
            count+=1

            if prev:
                # if theres prev we need to push onto max_heap for the next iteration
                heapq.heappush(max_heap,prev)
                prev=None
            # only set prev if the count isnt 0, here is where we hold
            if count!=0:
                prev = [count,char]
        return res

"""
Iteration 1. : prev = [-3,c] max_heap = [-1,d] res = c
Iteration 2. : prev = None max_heap = [-3,c] = res = cd
Iteration 3. : prev = [-2,c] res = cdc
Iteration 4. : 
"""
