"""
Reconstruct Itinerary
@ Graph + Euler Path
@ First, u must understand the problem: All tickets form at least one valid itinerary.
  Then, u understand what is Euler path: to go through each edge just once, with nodes being visited several times.
  Third, for there must exists at least one valid Euler path, u need to know how to get the Euler path.
@ For this problem: We greedy to go as far as we can, once got stuck, then pop(to start from the former point)
  and the stuck node will be the new destination.
"""


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        neighbors = {}
        # reverse as we always update by pop()
        for s, e in sorted(tickets, reverse=True):
            if s not in neighbors:
                neighbors[s] = []
            neighbors[s].append(e)
        routine, stack = [], ["JFK"]
        while stack:
            while neighbors.get(stack[-1], None):
                stack.append(neighbors[stack[-1]].pop())
            # once got stuck, the stuck node will be the new destination, then we can append it to result(reversed).
            routine.append(stack.pop())
        return routine[::-1]
