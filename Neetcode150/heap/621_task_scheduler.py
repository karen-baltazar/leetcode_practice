from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)  # Count frequency of each task
        max_heap = [-freq for freq in task_count.values()]  # Max-heap to store task frequencies
        heapq.heapify(max_heap)  # Transform list into a heap

        time = 0  # Time counter
        wait_queue = deque()  # Queue to hold tasks waiting for cooldown

        while max_heap or wait_queue:
            time += 1  # Increment time for each cycle

            if max_heap:
                freq = 1 + heapq.heappop(max_heap)  # Get the most frequent task
                if freq:  # If there are remaining tasks
                    wait_queue.append([freq, time + n])  # Add to wait queue with cooldown time

            if wait_queue and wait_queue[0][1] == time:  # If a task is ready to be re-added
                heapq.heappush(max_heap, wait_queue.popleft()[0])  # Re-add to heap
        
        return time  # Total time taken
