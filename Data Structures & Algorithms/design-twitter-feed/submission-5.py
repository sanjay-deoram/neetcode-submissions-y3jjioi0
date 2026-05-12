class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # userId -> list of [count, tweetIds] 
        self.followMap = defaultdict(set) # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count,tweetId])
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        res = []
        # adding yourself to the list
        self.followMap[userId].add(userId)
        for follower in self.followMap[userId]:
           if follower in self.tweetMap:
            last_tweet_index = len(self.tweetMap[follower])-1
            count, tweetId = self.tweetMap[follower][last_tweet_index]
            # pushes info, and the NEXT last tweet 
            heapq.heappush(minHeap,[count, tweetId, follower, last_tweet_index-1])
            
        while minHeap and len(res)<10:
            count, tweetId, follower, last_tweet_idx = heapq.heappop(minHeap)
            res.append(tweetId)
            if last_tweet_idx >=0:
                count, tweetId = self.tweetMap[follower][last_tweet_idx]
                heapq.heappush(minHeap,[count, tweetId, follower, last_tweet_idx - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)