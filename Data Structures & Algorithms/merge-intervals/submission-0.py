class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # when iterating interval, tyr to compare w/ the prev one?
        # use result to save the new interval (whether merged or not)
        
        intervals.sort() # make sure it's sorted
        result = [intervals[0]]

        for start, end in intervals[1:]:
            prev_start, prev_end = result[-1] # 每次要比較的都是目前最新的result

            # 每次都跟前一個interval 比較
            # 1. 沒有overlap:
            if start > prev_end:
                result.append([start, end])

            else:
                result[-1][1] = max(end, prev_end)

        return result