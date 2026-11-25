class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not newInterval:
            return intervals

        # loop through intervals
        # add to new list
        # if overlaps with new interval expand new interval
        # once no longer overlapping add new interval
        # then add rest of intervals

        res = []
        n = len(intervals)

        if n <= 0:
            return [newInterval]

        # [1,3] [2,5]

        newStart, newEnd = newInterval


        for i in range(n):
            start, end = intervals[i]

            # completely before
            if end < newStart:
                res.append(intervals[i])
            # completely after
            elif start > newEnd:
                res.append([newStart, newEnd])
                res.extend(intervals[i:])
                return res

            else:
                newStart = min(newStart, start)
                newEnd = max(newEnd, end)            

        res.append([newStart, newEnd])
        return res


        
        