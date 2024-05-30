from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a map to store prerequisites for each course
        preMap = {i: [] for i in range(numCourses)}

        # Populate the prerequisites map
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Set to keep track of courses along the current DFS path
        visitSet = set()

        # Depth-First Search (DFS) function to detect cycles
        def dfs(crs):
            # If the course is already in the current DFS path, a cycle is detected
            if crs in visitSet:
                return False
            # If the course has no prerequisites, it can be completed
            if preMap[crs] == []:
                return True

            # Add the course to the current DFS path
            visitSet.add(crs)

            # Recursively visit all prerequisites
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            # Remove the course from the current DFS path
            visitSet.remove(crs)
            # Mark the course as completed by emptying its prerequisites
            preMap[crs] = []
            return True
        
        # Check each course using DFS
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True