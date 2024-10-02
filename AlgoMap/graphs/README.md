| Problem Number | Problem Name | Explanation | Code |
|----------------|-------------------------|-------------------------------------|-----------------------------|
| 1971 | [Find if Path Exists in Graph](#1971-find-if-path-exists-in-graph) | [Explanation](#1971-find-if-path-exists-in-graph) | [Python Code](./1971_valid_path.py)       |

## 1971. Find if Path Exists in Graph

**Description**:
Given an undirected graph represented as `n` nodes and a list of edges, determine if there is a valid path between two given nodes, `src` and `dst`.

**Example**:
```plaintext
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: False
Explanation: There is no path from node 0 to node 5.
```

**Solution**:
This problem is solved using Depth-First Search (DFS):
- Build the graph using an adjacency list.
- Traverse the graph starting from the source node using DFS.
- Check if the destination node can be reached during the DFS traversal.

[Link to code](./1971_valid_path.py)

**Notes**:
- Time complexity: O(V + E), where V is the number of vertices (nodes) and E is the number of edges. This is because we visit each node and edge once.
- Space complexity: O(V), due to the space needed for the adjacency list and the visited set.