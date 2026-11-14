from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # use maxheap to manage the task -> do the one that needs to do the most first
        # use queue to store how long the cool down time need

        # 1. build the heap
        count = Counter(tasks)

        maxheap = [-cnt for cnt in count.values()]
        heapq.heapify(maxheap)

        cool_down_queue = deque() # (-cnt, how many time left)
        time = 0

        # 2. start counting time
        while maxheap or cool_down_queue:
            time += 1

            # if some task's cool down is over -> add to maxheap
            while cool_down_queue and cool_down_queue[0][1] <= time:
                cnt, available_time = cool_down_queue.popleft()
                heapq.heappush(maxheap, cnt)

            # start getting heap
            if maxheap:
                cnt = heapq.heappop(maxheap)
                cnt += 1
                
                # if its task is not done
                if cnt < 0:
                    cool_down_queue.append([cnt, time+n+1])

        return time





