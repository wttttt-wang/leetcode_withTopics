"""
Insert Delete GetRandom O(1) - Duplicates allowed
@ Design + Hash
"""


class RandomizedCollection(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums, self.sets = [], {}  # set of set

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.sets:
            self.sets[val].add(len(self.nums))
            self.nums.append(val)
            return False
        else:
            self.sets[val] = {len(self.nums)}
            self.nums.append(val)
            return True

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.sets:
            inds = self.sets[val]
            ind = inds.pop()
            if not inds:
                self.sets.pop(val)
            if ind != len(self.nums) - 1:
                self.nums[ind] = self.nums[-1]
                self.sets[self.nums[ind]].remove(len(self.nums) - 1)
                self.sets[self.nums[ind]].add(ind)
            self.nums.pop()
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        if not self.nums:
            return
        return self.nums[random.randint(0, len(self.nums) - 1)]
