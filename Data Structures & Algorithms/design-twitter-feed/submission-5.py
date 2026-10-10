class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        heap = []

        users = {userId} | self.followers[userId]

        for user in users:
            idx = len(self.tweets[user]) - 1

            if idx >= 0:
                heapq.heappush(heap, (*self.tweets[user][idx], user, idx))

        while len(feed) < 10 and heap:
            (_, tweet, user, idx) = heapq.heappop(heap)
            feed.append(tweet)

            if idx > 0:
                heapq.heappush(heap, (*self.tweets[user][idx - 1], user, idx - 1))

        return feed


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
        
