"""
All O`one Data Structure
@ Design + Hash + LinkedList: 1. Use double linked list to link occur numbers.
                              2. For each linked node with an occur number, along with a hashSet containing keys.
                              3. For all keys, use 'keys' to map from key to linked node.
@ It's really not easy to ac this problem. orz...
"""


class ListNode(object):
    def __init__(self, val):
        self.val, self.next, self.prev = val, None, None
        self.elements = set()


class AllOne(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = {}
        self.head, self.tail = ListNode(0), ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key in self.keys:
            cnt = self.keys[key].val
            self.keys[key].elements.remove(key)
            if not self.keys[key].elements:
                self.removeNode(self.keys[key])
                self.addTo(self.keys[key].prev, key, cnt + 1)
            else:
                self.addTo(self.keys[key], key, cnt + 1)
        else:
            self.addTo(self.head, key, 1)

    def addTo(self, node, key, val):
        if node.next and val == node.next.val:
            node.next.elements.add(key)
            self.keys[key] = node.next
        else:
            newNode = ListNode(val)
            newNode.elements.add(key)
            newNode.prev, newNode.next = node, node.next
            node.next.prev = newNode
            node.next = newNode
            self.keys[key] = newNode

    def addBefore(self, node, key, val):
        if node.val == val:
            node.elements.add(key)
            self.keys[key] = node
        else:
            newNode = ListNode(val)
            newNode.elements.add(key)
            newNode.prev, newNode.next = node, node.next
            node.next.prev = newNode
            node.next = newNode
            self.keys[key] = newNode

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.keys:
            cnt = self.keys[key].val
            self.keys[key].elements.remove(key)
            if not self.keys[key].elements:
                self.removeNode(self.keys[key])
            if cnt > 1:
                self.addBefore(self.keys[key].prev, key, cnt - 1)
            else:
                self.keys.pop(key)

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.tail.prev.val == 0:
            return ""
        res = self.tail.prev.elements.pop()
        self.tail.prev.elements.add(res)
        return res

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.head.next.val == 0:
            return ""
        res = self.head.next.elements.pop()
        self.head.next.elements.add(res)
        return res

    def removeNode(self, node):
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail.prev = node.prev


so = AllOne()
so.inc("h")
so.inc("h")
so.dec("h")
so.dec("h")
so.dec("h")
