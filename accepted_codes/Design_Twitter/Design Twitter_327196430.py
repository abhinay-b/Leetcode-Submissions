from collections import defaultdict,deque
import heapq
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
#       A dictionary to store the userwise-tweets in a queue manner
        self.tweets = defaultdict(deque)
#       A dictionary to store the userwise-followees in a set
        self.followees = defaultdict(set)
#       An integer timer to order the tweets of various users
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
#       A user is a follower of himself. So add him to the followees table
        self.followees[userId].add(userId)
#       Add the new tweet to the queue with the current timer value
        self.tweets[userId].appendleft((self.timer,tweetId))
#       Discard older tweets if the queue is larger than the limit size
        if len(self.tweets[userId]) > 10:
            oldTweet = self.tweets[userId].pop()
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news 
            feed must be posted by users who the user followed or by the user herself. Tweets 
            must be ordered from most recent to least recent.
        """
#       Use a heap to store 10 tweets and update it as and when newer tweets exist (similar to 
    k largest numbers)
        heap = []
        for user in self.followees[userId]:
            for tweet in self.tweets[user]:
                if len(heap) < 10:
                    heapq.heappush(heap,tweet)
#               Check the age of the tweet. Break from followee if current tweet is older than 
    the min heap top element
                elif tweet[0] > heap[0][0]:
                    heapq.heappushpop(heap,tweet)
                else:
                    break
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
#       Heap contained 10 most recent tweets but in a min heap manner. So res contains it in 
    increasing order of age
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.followees[followerId] and followerId != followeeId:
            self.followees[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
