"""
Linked List Random Node
@ Reservoir Sampling: Use reservoir sampling can avoid repeat visit.
"""


class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        if not self.head:
            return
        candidate, pv = self.head.val, 1
        tmp = self.head
        while tmp:
            if random.randint(1, pv) == 1:
                candidate = tmp.val
            tmp = tmp.next
            pv += 1
        return candidate
