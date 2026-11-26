class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key = lambda i: i[1])

        n = len(intervals)
        prev_end = intervals[0][1]
        for i in range(1, n):
            if prev_end > intervals[i][0]:
                res += 1
            else:
                prev_end = intervals[i][1]


        return res