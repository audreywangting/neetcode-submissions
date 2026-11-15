import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # use heap to manage execute the one with the most tasks
        # use deque to store (left_cnt, available_time)

        count = Counter(tasks)
        maxheap = [-cnt for cnt in count.values()]
        heapq.heapify(maxheap)
        q = deque()
        time = 0

        # 1. take the maxheap[0] as the one needed to be dealed w/ first
        while maxheap or q:
            time += 1
            
            # 1. check if maxheap is not null
            if maxheap:
                cnt = heapq.heappop(maxheap)
                
                # one task is done
                cnt += 1

                # if there's remaining task
                if cnt < 0:
                    q.append([cnt, time+n]) # add interval

            # 2. check if cool down is over
            while q and q[0][1] <= time:
                cnt, available_time = q.popleft()
                heapq.heappush(maxheap, cnt)

        return time

