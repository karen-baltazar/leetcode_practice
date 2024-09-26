# Problems

| Problem Number | Problem Name                                  | Explanation                                      | Code                                           |
|----------------|-----------------------------------------------|--------------------------------------------------|------------------------------------------------|
| 703  | [Kth Largest Element in a Stream](#703-kth-largest-element-in-a-stream) | [Explanation](#703-kth-largest-element-in-a-stream) | [Python Code](./703_kth_largest_element_stream.py) |
| 621  | [Task Scheduler](#621-task-scheduler) | [Explanation](#621-task-scheduler) | [Python Code](./621_task_scheduler.py) |

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