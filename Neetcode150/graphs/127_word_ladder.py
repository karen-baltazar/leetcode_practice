class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Check if the endWord exists in the wordList, if not return 0
        if endWord not in wordList:
            return 0

        # Dictionary to store patterns and corresponding words
        patternDict = defaultdict(list)
        wordList.append(beginWord)

        # Build pattern dictionary by replacing each character with "*"
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                patternDict[pattern].append(word)

        # Set for visited words and queue for BFS
        visited = set([beginWord])
        queue = deque([beginWord])
        transformations = 1

        # BFS to find the shortest transformation sequence
        while queue:
            for _ in range(len(queue)):
                currentWord = queue.popleft()

                if currentWord == endWord:
                    return transformations
                
                # Explore neighboring words via pattern matching
                for i in range(len(currentWord)):
                    pattern = currentWord[:i] + "*" + currentWord[i + 1:]
                    for neighborWord in patternDict[pattern]:
                        if neighborWord not in visited:
                            visited.add(neighborWord)
                            queue.append(neighborWord)
            transformations += 1

        # If no transformation is possible, return 0
        return 0
