from collections import defaultdict
import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.user_follow = defaultdict(set)  # Tracks follow relationships
        self.user_tweets = defaultdict(list)  # Tracks user tweets with timestamps
        self.time = 0  # Global timestamp for tweets
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        # Add tweet with timestamp
        self.user_tweets[userId].append((self.time, tweetId))
        self.time -= 1  # Use negative time to prioritize recent tweets

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []  # Stores the feed result
        max_heap = []  # Max heap to track latest tweets

        self.user_follow[userId].add(userId)  # Ensure user follows themselves
        # Gather the latest tweet from each followed user
        for followeeId in self.user_follow[userId]:
            if followeeId in self.user_tweets:
                idx = len(self.user_tweets[followeeId]) - 1
                time, tweetId = self.user_tweets[followeeId][idx]
                max_heap.append((time, tweetId, followeeId, idx - 1))

        heapq.heapify(max_heap)  # Convert to max heap
        # Extract up to 10 latest tweets
        while max_heap and len(res) < 10:
            time, tweetId, followeeId, idx = heapq.heappop(max_heap)
            feed.append(tweetId)
            # Add next tweet of the same user if exists
            if idx >= 0:
                next_time, next_tweetId = self.user_tweets[followeeId][idx]
                heapq.heappush(max_heap, (next_time, next_tweetId, followeeId, idx - 1))
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follow[followerId].add(followeeId)  # Add followee to follower's list

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove followee only if it's not self-follow
        if followeeId in self.user_follow[followerId] and followeeId != followerId:
            self.user_follow[followerId].remove(followeeId)
