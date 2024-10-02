from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prereqs: List[List[int]]) -> bool:
        # Create a prerequisite map using defaultdict
        prereq_map = defaultdict(list)

        # Fill the prerequisite map with course dependencies
        for crs, pre in prereqs:
            prereq_map[crs].append(pre)

        # Set to track the courses currently being visited in the DFS path
        visiting = set()

        # Helper function to perform DFS to detect cycles
        def dfs(crs):
            # If the course is already in the visiting path, we have a cycle
            if crs in visiting:
                return False
            # If the course has no prerequisites left, we can finish it
            if prereq_map[crs] == []:
                return True

            # Mark the course as being visited
            visiting.add(crs)

            # Perform DFS on all the prerequisites of the current course
            for pre in prereq_map[crs]:
                if not dfs(pre):
                    return False

            # Once all prerequisites are checked, remove the course from the visiting path
            visiting.remove(crs)
            # Mark the course as completed by emptying its prerequisites
            prereq_map[crs] = []

            return True

        # Check every course to see if we can complete it without encountering a cycle
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
