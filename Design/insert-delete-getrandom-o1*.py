"""
Insert Delete GetRandom O(1)
@ Design + Hash
@ Note: How to support O(1) remove for an array? --> replace with tail.
        So the corner case is when the to-removed element be the tail
"""
import random


class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums, self.sets = [], {}  # sets

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.sets:
            self.sets[val] = len(self.nums)
            self.nums.append(val)
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.sets:
            ind = self.sets.pop(val)
            # to support O(1) delete
            self.nums[ind], self.nums[-1] = self.nums[-1], self.nums[ind]
            if self.nums[ind] != val:  # Attention: Important here!!!
                self.sets[self.nums[ind]] = ind
            self.nums.pop()
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if not self.nums:
            return
        return self.nums[random.randint(0, len(self.nums) - 1)]


so = RandomizedSet()
so.insert(3)
so.remove(3)
so.remove(3)
so.remove(3)
so.insert(1)
so.insert(-3)
so.remove(-2)
