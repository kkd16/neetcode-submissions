class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n <= 1:
            return intervals

        intervals.sort()
        
        res = [intervals[0]]
        for i in range(1, n):
            new_start, new_end = intervals[i]
            old_start, old_end = res[-1]

            if new_start <= old_end:
                res[-1][1] = max(new_end, old_end)
            else:
                res.append(intervals[i])

        return res




