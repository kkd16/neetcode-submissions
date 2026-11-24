class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # [[1,3],[1,5],[5,7]]

        # res:
        # [1,3]
        # [1,5]
        # [1,7]

        # if len <= 1 return intervals
        # sort intervals by non decreasing start time 
        # copy first interval to the res array
        # loop through intervals starting at interval 1 (0 indexed)
        # then if interval i's start time is <= interval res[-1] end time
        # modify end of interval res[-1] to be the greater of endpoints
        # move on 

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




