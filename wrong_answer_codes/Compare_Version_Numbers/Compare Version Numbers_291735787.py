class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        idx1 = idx2 = 0
        version1 = version1.split('.')
        version2 = version2.split('.')
        while idx1 < len(version1) and idx2 < len(version2) and version1[idx1] == 
            version2[idx2]:
            idx1 += 1
            idx2 += 1
        if idx1 < len(version1) and idx2 < len(version2):
            if version1[idx1] < version2[idx2]:
                return -1
            else:
                return 0
        elif idx2 < len(version2):
            if idx2 == len(version2)-1 and int(version2[idx2]) == 0:
                return 0
            return -1
        return 1
            
