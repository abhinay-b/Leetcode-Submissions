class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = result = ""
        for element in s:
            idx = temp.find(element)
            if idx != -1:
                if len(result) < len(temp):
                    result = temp
                temp = temp[idx+1: ]
                
            temp += element
        if len(result) < len(temp):
            result = temp

        return len(result)
