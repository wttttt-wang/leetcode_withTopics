"""
Design Twitter
@ Design: @ Heap + Hash + oop (It's better to solve this problem using object-oriented programing.)
          We need to maintain a global order id for getNewsFeed.
@ Note: Can one follow himself? This is a good question to ask on an interview.
"""

from collections import deque
from heapq import *


class Tweet(object):
    def __init__(self, tweetId, orderId):
        self.tweetId, self.orderId = tweetId, orderId


class TwitterUser(object):
    def __init__(self, userId):
        self.userId = userId
        self.tweets = deque()
        self.follows = set()

    def post(self, tweet):
        while len(self.tweets) >= 10:
            self.tweets.popleft()
        self.tweets.append(tweet)

    def addFollow(self, userId):
        self.follows.add(userId)

    def removeFollow(self, userId):
        if userId in self.follows:
            self.follows.remove(userId)

    def getFollows(self):
        return self.follows

    def getTweets(self):
        return list(self.tweets)


class Twitter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = {}
        self.orderId = 0   # we need to maintain a global order Id.

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.users:
            self.users[userId] = TwitterUser(userId)
        tweet = Tweet(tweetId, self.orderId)
        self.orderId += 1
        self.users[userId].post(tweet)

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.users:
            self.users[userId] = TwitterUser(userId)
        tweets = []
        if userId not in self.users[userId].getFollows():  # Can one follow himself? This is a good question to ask.
            tweets = self.users[userId].getTweets()
        for user in self.users[userId].getFollows():
            tweets += self.users[user].getTweets()
        tmp = nlargest(10, tweets, key=lambda x: x.orderId)
        return [x.tweetId for x in tmp]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.users:
            self.users[followerId] = TwitterUser(followerId)
        if followeeId not in self.users:
            self.users[followeeId] = TwitterUser(followeeId)
        self.users[followerId].addFollow(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.users:
            self.users[followerId].removeFollow(followeeId)
