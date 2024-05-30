class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create a dictionary to store the prerequisites for each course
        preMap = {i: [] for i in range(numCourses)}

        # Fill the dictionary with the prerequisites for each course
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Sets to keep track of visited courses and the current cycle
        visit, cycle = set(), set()
        output = []

        def dfs(crs):
            # If the course is in the current cycle, a cycle is detected and we return False
            if crs in cycle:
                return False
            # If the course has already been visited, no need to process it again
            if crs in visit:
                return True

            # Add the course to the current cycle
            cycle.add(crs)

            # Perform DFS on the prerequisites of the current course
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            # Remove the course from the current cycle and mark it as visited
            cycle.remove(crs)
            visit.add(crs)
            # Add the course to the output
            output.append(crs)
            return True

        # Perform DFS on each course
        for crs in range(numCourses):
            if not dfs(crs):
                return []

        # Return the output in reverse order (topological order)
        return output
