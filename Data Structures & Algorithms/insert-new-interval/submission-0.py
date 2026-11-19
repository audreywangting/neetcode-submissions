class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # check if newinterval is overlapped in any interval
            # start of interval < start of newinterval < end of newinterval 

        # if overlapped: merged into a new interval
        # if not: added as a new interval

        result = []

        for start, end in intervals:
            # overlap
            # 1. current interval 在 newInterval 左邊
            if end < newInterval[0]:
                result.append([start, end])

            # 2. current interval 在 newInterval 右邊
            elif start > newInterval[1]:
                result.append(newInterval)
                newInterval = [start, end]

            # 3. current interval overlap newInterval 
            else:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])  
        
        # 因為在 2. 時把newInterval當作暫存區，所以最後會有剩下一個要存
        result.append(newInterval)

        return result

