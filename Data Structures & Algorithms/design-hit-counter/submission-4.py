class HitCounter:

    def __init__(self):
        self.q =[]

    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        count = 0

        for time in self.q:
            diff = timestamp - time
            if diff < 300:
                count+=1
        return count


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
