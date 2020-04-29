from collections import defaultdict,deque
import heapq
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = defaultdict(deque)
        self.followees = defaultdict(set)
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.followees[userId].add(userId)
        self.tweets[userId].append((self.timer,tweetId))
        if len(self.tweets[userId]) > 10:
            oldTweet = self.tweets[userId].popleft()
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news 
            feed must be posted by users who the user followed or by the user herself. Tweets 
            must be ordered from most recent to least recent.
        """
        heap = []
        for user in self.followees[userId]:
            for tweet in self.tweets[user]:
                if len(heap) < 10:
                    heapq.heappush(heap,tweet)
                elif tweet[0] > heap[0][0]:
                    heapq.heappushpop(heap,tweet)
                else:
                    break
        return [tweet[1] for tweet in heap[::-1]]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
