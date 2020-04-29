class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        pref = strs[0]
        if len(strs) == 1:
            return pref
        for word in strs:
            while pref not in word:
                pref = pref[:-1]
            if len(pref) == 0:
                return pref
        return pref
        
