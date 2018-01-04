"""
Insert Interval
@ Sort
"""


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        left, right = 0, len(intervals)
        for i in range(len(intervals)):
            if intervals[i].end < newInterval.start:
                left += 1
            elif intervals[i].start > newInterval.end:
                right = i
                break
            else:
                newInterval.start = min(newInterval.start, intervals[i].start)
                newInterval.end = max(newInterval.end, intervals[i].end)
        intervals[left:right] = [newInterval]
        return intervals

