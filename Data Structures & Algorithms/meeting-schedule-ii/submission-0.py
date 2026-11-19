import heapq
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # 拿heap存結束時間，heap[0]會是最早結束的會議，每次都和下一個開始時間比
        # 如果比較小，代表結束，就不用再借新的會議室
        intervals.sort(key=lambda x: x.start)

        minheap = []

        # iterate thrun meetings
        for interval in intervals:
            start = interval.start
            end = interval.end

            # 直接 reuse 會議室
            if minheap and minheap[0] <= start:
                heapq.heappop(minheap)

            heapq.heappush(minheap, end) 

        return len(minheap)

        