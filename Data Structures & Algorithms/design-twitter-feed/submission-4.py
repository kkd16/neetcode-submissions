class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        out = []
        maxHeap = []

        idx = len(self.tweets[userId]) - 1

        if idx >= 0:
            heapq.heappush(maxHeap, (*self.tweets[userId][idx], userId, idx))

        for followee in self.followers[userId]:
            idx = len(self.tweets[followee]) - 1

            if idx >= 0:
                heapq.heappush(maxHeap, (*self.tweets[followee][idx], followee, idx))

        while len(out) < 10 and maxHeap:
            (c, tId, uId, idx) = heapq.heappop(maxHeap)
            out.append(tId)

            if idx > 0:
                heapq.heappush(maxHeap, (*self.tweets[uId][idx - 1], uId, idx - 1))

        return out


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
        
