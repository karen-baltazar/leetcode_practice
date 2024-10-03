class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Hint: This problem is solved using Dijkstra's algorithm to find the shortest time it takes for the signal to reach all nodes.
        # The graph is represented as an adjacency list, and we use a min-heap to efficiently track the smallest signal propagation time.

        visited = set()  # Tracks nodes that have been processed
        min_heap = [(0, k)]  # Stores (time, node) pairs, starting from the source node k
        graph = defaultdict(list)  # Adjacency list representation of the graph
        max_time = 0  # Tracks the maximum time to reach all nodes

        # Build the graph from input times
        for u, v, w in times:
            graph[u].append((w, v))

        # Process nodes using a priority queue (min-heap)
        while min_heap:
            prev_time, node = heapq.heappop(min_heap)

            if node in visited:  # Skip if node is already visited
                continue

            visited.add(node)
            max_time = max(max_time, prev_time)

            # Push neighbors into the heap with their cumulative signal time
            for time, nei in graph[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (time + prev_time, nei))

        # If all nodes were visited, return the max signal time; otherwise, return -1
        return max_time if len(visited) == n else -1
