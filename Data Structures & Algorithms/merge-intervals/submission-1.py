class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals, key = lambda x : x[0])

        
        out = []
        out.append(intervals[0])

        for i in range(len(intervals) - 1):

            if out[len(out) - 1][1] >= intervals[i + 1][0]:
                
                out[len(out) - 1][1] = max(out[len(out) - 1][1], intervals[i + 1][1])

            else:
                out.append(intervals[i+1])


            
        return out
        