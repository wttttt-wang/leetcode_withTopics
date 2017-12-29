"""
Non-overlapping Intervals
@ Greedy: The key point is try to select the interval with smaller end.
          So we sort by interval.end, and try to select the selectable interval with smaller end first.
@ O(NlogN) time for sorting.
"""


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.end)
        right = intervals[0].start
        res = 0
        for inter in intervals:
            if inter.start >= right:
                right = inter.end
            else:
                res += 1
        return res
