"""
LRU Cache
@ Design: 1. Two hashMap + One linkedList
          2. should be careful when dealing with hashMap in case of 'keyError'
          3. reminder to update self.tail
"""


class ListNode(object):
    def __init__(self, val):
        self.val, self.next = val, None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.k2v, self.k2node = {}, {}
        self.head, self.capacity = ListNode(0), capacity
        self.tail = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.k2v:
            return -1
        val = self.k2v[key]
        node = self.removeNode(self.k2node[key].next)
        self.addAhead(node, val)
        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.k2v:
            node = self.removeNode(self.k2node[key].next)
            self.addAhead(node, value)
            return
        if len(self.k2v) == self.capacity:
            self.removeNode(self.tail)
        self.addAhead(ListNode(key), value)

    def removeNode(self, node):
        if node.next:
            self.k2node[node.next.val] = self.k2node[node.val]
        else:
            self.tail = self.k2node[node.val]
        self.k2node[node.val].next = node.next
        self.k2node.pop(node.val)
        self.k2v.pop(node.val)
        return node

    def addAhead(self, node, value):
        if self.head.next:
            self.k2node[self.head.next.val] = node
        else:
            self.tail = node
        node.next = self.head.next
        self.head.next = node
        self.k2node[node.val] = self.head
        self.k2v[node.val] = value
