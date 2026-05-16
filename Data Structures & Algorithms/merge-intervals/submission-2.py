class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        out = []
        out.append(intervals[0])

        for start, end in intervals[1:]:

            if out[-1][1] >= start:
                
                out[-1][1] = max(out[-1][1], end)

            else:
                out.append([start, end])


            
        return out
        