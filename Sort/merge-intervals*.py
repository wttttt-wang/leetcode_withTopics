"""
Merge Intervals
@ Sort: The key point is how to sort(the key of sorting).
        After sort by start, for interval b comes after a(a.start <= b.start),
        there is no way for b to updating the results before a.
"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        results = []
        intervals.sort(key=lambda x: x.start)
        for tmp in intervals:
            if results and results[-1].end >= tmp.start:
                tt = results.pop()
                results.append(Interval(tt.start, max(tt.end, tmp.end)))
            else:
                results.append(tmp)
        return results
