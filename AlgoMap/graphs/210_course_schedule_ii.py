from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create a prerequisite map using defaultdict
        prereq_map = defaultdict(list)

        # Fill the prerequisite map with course dependencies
        for crs, pre in prerequisites:
            prereq_map[crs].append(pre)

        # Sets to track visited nodes and those in the current DFS path (cycle check)
        visited = set()
        path = set()
        output = []

        # Helper function to perform DFS to detect cycles and build the course order
        def dfs(crs):
            # If the course is already in the current path, we found a cycle
            if crs in path:
                return False
            # If the course is already visited, skip it
            if crs in visited:
                return True

            # Mark the course as being part of the current path
            path.add(crs)

            # Perform DFS on all prerequisites for the current course
            for pre in prereq_map[crs]:
                if not dfs(pre):
                    return False

            # Remove the course from the current path and mark it as visited
            path.remove(crs)
            visited.add(crs)
            # Append the course to the output order
            output.append(crs)

            return True

        # Check every course to build the course order
        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return output
