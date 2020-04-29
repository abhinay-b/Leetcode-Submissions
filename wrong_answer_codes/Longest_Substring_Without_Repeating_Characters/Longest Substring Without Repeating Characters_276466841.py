class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subset =  set()
        backup = set()
        for element in s:
            if element in subset:                
                if len(backup) < len(subset):
                    backup.clear()
                    backup.update(subset)
                subset.clear()
            subset.add(element)
        return len(backup)
