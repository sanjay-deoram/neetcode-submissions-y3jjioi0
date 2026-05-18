class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # max heap and  queue
        task_map = Counter(tasks)
        max_heap = [-x for x in task_map.values()]
        heapq.heapify(max_heap)
        q = deque() # [count, idletime]
        time=0
        
        while max_heap or q:
            time+=1
            
            if max_heap:
                count = 1 + heapq.heappop(max_heap)
                if count:
                    q.append([count, time+n])
            
            if q and q[0][1]==time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time
