class Twitter:

    def __init__(self):
        self.count = 0 
        self.tweetMap = defaultdict(list) # userId -> list of [count, tweetIds] {1:[[0,10],[2,10]]}
        self.followMap = defaultdict(set) # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count,tweetId])
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                last_tweet_index = len(self.tweetMap[followeeId])-1
                count, tweetId = self.tweetMap[followeeId][last_tweet_index]
                heapq.heappush(max_heap,[count, tweetId, followeeId, last_tweet_index-1])
        
        feed = []
        while max_heap and len(feed)<10:
            count, tweetId, followeeId, last_tweet_index = heapq.heappop(max_heap)
            feed.append(tweetId)

            if last_tweet_index >= 0:
                count, tweetId = self.tweetMap[followeeId][last_tweet_index]
                heapq.heappush(max_heap, [count, tweetId, followeeId, last_tweet_index-1])

        return feed



    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
