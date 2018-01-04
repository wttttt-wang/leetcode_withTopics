"""
Palindrome Linked List
@ Two pointers + Linked List
@ To solve this problem with O(1) space, we have to reverse half of the list.
  To simplify, we reverse the left half when find mid
@ Note: the head of right half is different for linked list with odd/even nodes.
"""


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        slow, fast = head, head
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            # reverse slow
            tmp = slow.next
            slow.next = rev
            rev = slow
            slow = tmp
        if fast:
            slow = slow.next   # Attention: for linked list with odd nodes!!!!!!!
        while slow:
            if slow.val != rev.val:
                return False
            slow, rev = slow.next, rev.next
        return True

