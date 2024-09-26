# Problems

| Problem Number | Problem Name                                  | Explanation                                      | Code                                           |
|----------------|-----------------------------------------------|--------------------------------------------------|------------------------------------------------|
| 703  | [Kth Largest Element in a Stream](#703-kth-largest-element-in-a-stream) | [Explanation](#703-kth-largest-element-in-a-stream) | [Python Code](./703_kth_largest_element_stream.py) |
| 621  | [Task Scheduler](#621-task-scheduler) | [Explanation](#621-task-scheduler) | [Python Code](./621_task_scheduler.py) |
| 355  | [Design Twitter](#355-design-twitter) | [Explanation](#355-design-twitter) | [Python Code](./355_design_twitter.py)         |
| 295  | [Find Median from Data Stream](#295-find-median-from-data-stream) | [Explanation](#295-find-median-from-data-stream) | [Python Code](./295_find_median_from_stream.py) |

## 703. Kth Largest Element in a Stream

**Description**:
Design a class to find the k-th largest element in a stream of numbers. The class should support adding new numbers to the stream.

**Example**:
```plaintext
Input: kthLargest = KthLargest(3, [4,5,8,2])
kthLargest.add(3)  # returns 4
kthLargest.add(5)  # returns 5
kthLargest.add(10) # returns 5
kthLargest.add(9)  # returns 8
kthLargest.add(4)  # returns 8
```

**Solution**:
We use a min-heap to keep track of the k largest elements. When a new number is added, if the heap contains fewer than k elements, we add it directly. If it’s larger than the smallest element in the heap (the root), we replace the smallest element. The k-th largest element is always at the root of the heap.

[Link to code](./703_kth_largest_element_stream.py)

**Notes**:
- Time complexity: O(log k) for adding each new element due to heap operations. The initialization takes O(n log k) where n is the number of initial elements.
- Space complexity: O(k) for storing the k largest elements in the heap.

## 621. Task Scheduler

**Description**:
Given a list of tasks represented by characters and a non-negative integer n representing the cooldown period between the same tasks, return the least number of units of time to finish all tasks.

**Example**:
```plaintext
Input: tasks = ["A", "A", "A", "B", "B", "B"], n = 2
Output: 8
Explanation: One possible way is: A -> B -> idle -> A -> B -> idle -> A -> B.
```

**Solution**:
We use a max-heap to keep track of task frequencies. The process consists of incrementing time in each cycle. If the heap has tasks, we pop the most frequent task and decrement its count. If it still has remaining instances, we add it to a wait queue with its next available time. After that, if the front of the wait queue has reached its cooldown time, we re-add it to the heap.

[Link to code](./621_task_scheduler.py)

**Notes**:
- Time complexity: O(m log m), where m is the number of unique tasks. Each task can be pushed and popped from the heap.
- Space complexity: O(m) for storing the task counts and wait queue.

## 355. Design Twitter

**Description**:
Design a simplified version of Twitter where users can post tweets, follow/unfollow other users, and retrieve the 10 most recent tweets from the user's news feed. Each tweet has a timestamp, and the news feed must show tweets from followed users in reverse chronological order.

**Example**:
```plaintext
Input: 
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]

Output: 
[null, null, [5], null, null, [6, 5], null, [5]]
```

The class should support the following methods:
1. `postTweet(userId, tweetId)`: Post a tweet by a user.
2. `getNewsFeed(userId)`: Retrieve the 10 most recent tweet IDs in the user's news feed.
3. `follow(followerId, followeeId)`: The user `followerId` follows the user `followeeId`.
4. `unfollow(followerId, followeeId)`: The user `followerId` unfollows `followeeId`.

**Solution**:
- A max-heap (priority queue) is used to track the latest tweets from each followed user.
- The `user_follow` dictionary stores the follow relationships, while `user_tweets` keeps a list of (time, tweetId) for each user.
- Each time a tweet is posted, the global `time` counter is decremented to ensure that more recent tweets appear first in the feed.
- To generate the news feed, the algorithm checks the last tweet of each followed user, then uses a heap to extract the 10 most recent tweets.

[Link to code](./355_design_twitter.py)

**Notes**:
- Time Complexity:
  - `postTweet`: O(1)
  - `getNewsFeed`: O(f + log k), where `f` is the number of followed users with tweets, and `k` is the number of tweets retrieved (at most 10).
  - `follow` and `unfollow`: O(1)
- Space Complexity: O(t + f), where `t` is the total number of tweets and `f` is the number of follow relationships.

## 295. Find Median from Data Stream

**Description**:  
The task is to find the median of a number stream. Numbers are being added continuously, and the goal is to design a data structure that efficiently finds the median at any given time.

**Example**:
```plaintext
Input: addNum(1), addNum(2), findMedian(), addNum(3), findMedian()
Output: 1.5, 2
Explanation: 
- After adding 1 and 2, the median is (1 + 2) / 2 = 1.5.
- After adding 3, the median is 2.
```

**Solution**:  
We use two heaps: 
- `max_heap` to store the smaller half of the numbers (negated values to simulate max heap behavior).
- `min_heap` to store the larger half.  
When adding a number, we ensure the balance between both heaps. The heaps maintain the order, making it easy to calculate the median depending on the heaps' sizes.

[Link to code](./295_find_median_from_stream.py)

**Notes**:
- Time Complexity: O(log n) per `addNum()` operation due to heap insertion, and O(1) for `findMedian()`.
- Space Complexity: O(n) where n is the total number of elements added, since each element is stored in one of the heaps.