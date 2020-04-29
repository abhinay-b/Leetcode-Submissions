class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
#         sort based on the start of the interval
        intervals.sort(key=lambda x: x[0])
        res = []
        idx = 1
        temp = intervals[0]
        while idx < len(intervals):
            if temp[0] <= intervals[idx][0] <= temp[1] or intervals[idx][0] <= temp[0] <= 
                intervals[idx][1]:
                temp[0],temp[1] = min(temp[0],intervals[idx][0]), max(temp[1]
                    ,intervals[idx][1])
            else:
                res.append(temp)
                temp = intervals[idx]
            idx += 1
        res.append(temp)
        return res
