"""
Copy List with Random Pointer
@ Linked List
"""


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        tmp = head
        while tmp:
            tmpNext = tmp.next
            tmp.next = RandomListNode(tmp.label)
            tmp.next.next = tmpNext
            tmp = tmpNext
        # 2. copy random
        tmp = head
        while tmp:
            if tmp.random:
                tmp.next.random = tmp.random.next  # Attention: random may point to None!!!
            tmp = tmp.next.next
        # 3. split to get final result
        dummy, tmp = RandomListNode(0), head
        tmpRes = dummy
        while tmp:
            tmpRes.next = tmp.next
            tmpRes = tmpRes.next
            tmp.next = tmp.next.next
            tmp = tmp.next
        return dummy.next

