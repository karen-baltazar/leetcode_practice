class Solution(object):
    def maxNumberOfBalloons(self, text):
        # Count frequency of relevant characters in text
        count = defaultdict(int)
        balloon = set('balloon')

        for c in text:
            if c in balloon:
                count[c] += 1
                
        # Check if all characters of "balloon" are present in text
        if any(c not in count for c in balloon):
            return 0
        else:
            # Return the minimum possible "balloon" that can be formed
            return min(count['b'], count['a'], count['l'] // 2, count['o'] // 2, count['n'])
