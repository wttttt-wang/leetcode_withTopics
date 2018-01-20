"""
Task Scheduler
@ Greedy + Heap + Hash: 1. The greedy way is obvious: choose the most left choose-able task.
                        2. But the way to implement is somewhat difficult.
                           2.1 use heap to select the left-most task.
                           2.2 use map to ensure we only add choose-able task to heap.
"""


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if not tasks:
            return 0
        occurs = {}
        for t in tasks:
            occurs[t] = occurs.get(t, 0) - 1
        heap = occurs.values()
        heapq.heapify(heap)
        availTasks = {}  # round: task (Note that this will be only one availTask will be added for each round)
        pround, res, left = 0, 0, len(tasks)
        while left > 0:
            # 1. if availTasks for this round
            if pround in availTasks:
                heapq.heappush(heap, -availTasks[pround])
            if heap:  # may be idle
                cnt = -heapq.heappop(heap)
                if cnt - 1 > 0:
                    availTasks[pround + n + 1] = cnt - 1
                left -= 1
            res += 1
            pround += 1
        return res
