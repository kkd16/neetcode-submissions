"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        sorted_intervals = sorted(intervals, key=lambda interval: interval.start)

        for i in range(len(intervals) - 1):
            if sorted_intervals[i].end > sorted_intervals[i + 1].start:
                return False

        return True