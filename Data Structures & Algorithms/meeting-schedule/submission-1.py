"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start) # 因為interval 是object, 所以要自定義

        for i in range(1, len(intervals)):
            curr_start = intervals[i].start
            prev_end = intervals[i-1].end

            # overlap
            if curr_start < prev_end:
                return False

        return True
