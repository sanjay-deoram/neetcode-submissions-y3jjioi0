class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # want max heap, want the most frequent values.
        taskMap = Counter(tasks)
        maxHeap = [-x for x in taskMap.values()]
        q = deque()
        time = 0
        heapq.heapify(maxHeap)

        while q or maxHeap:
            time+=1
            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    q.append([count,time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time
