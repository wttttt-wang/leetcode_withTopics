"""
Matchsticks to Square
@ DFS
@ Note to sort appropriately to skip unnecessary recursion.
"""


class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        s = sum(nums)
        sideLen = s / 4
        if s % 4 or max(nums) > sideLen:
            return False
        target = [sideLen] * 4
        nums.sort(reverse=True)  # Attention: For speeding up, sort & reverse sort are really necessary.
        return self.helper(nums, target, 0)

    def helper(self, nums, target, startInd):
        if startInd == len(nums):
            return sum(target) == 0
        visited = set()  # to skip repeat recursion: for target may contains duplicates which need no more recursion.
        for j in range(4):
            if nums[startInd] <= target[j] and target[j] not in visited:
                visited.add(target[j])
                target[j] -= nums[startInd]
                if self.helper(nums, target, startInd + 1):
                    target[j] += nums[startInd]
                    return True
                target[j] += nums[startInd]
        return False
