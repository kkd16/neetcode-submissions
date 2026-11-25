class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # [1,3][1,2][2,4][1,4]
        # [1,2][1,3][2,4][1,4]

        # 12345 
        # --
        # ---
        #  ---
        # ----


        # sort by end
        # when encountering an overlap remove the one with the latest end date
        # overlaps only need to nbe done by each one but 

        res = 0
        intervals.sort(key = lambda i: i[1])

        n = len(intervals)
        i = 0

        while i < n - 1:
            if intervals[i][1] > intervals[i + 1][0]:
                intervals.pop(i + 1)
                n -= 1
                res += 1
            else:
                i += 1
        
        return res


        