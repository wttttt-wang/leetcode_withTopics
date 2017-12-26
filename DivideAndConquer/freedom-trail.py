"""
Freedom Trail
@ Divide And Conquer  + dynamic programming / memorization
@ O(N * K) time  & space
"""
import sys


class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        if not ring or not key:
            return 0
        # dp[i][j] = max(dp[i + 1][x] + abs(j - x) + 1 for s in steps)
        steps = self.getSteps(ring, set(key))  # steps needed from ring to k in key
        return self.dpHelper(ring, key, steps, {}, 0, 0)

    def dpHelper(self, ring, key, steps, dp, startInd, state):
        if startInd == len(key):
            return 0
        if (startInd, state) not in dp:
            tmpMin = sys.maxint
            for step in steps[key[startInd]]:
                # to calculate the step needed from current 'state'
                step -= state
                if step + len(ring) < abs(step):
                    step += len(ring)
                elif abs(step - len(ring)) < abs(step):
                    step -= len(ring)
                # to calculate the new state
                newState = state + step
                newState = newState + len(ring) if newState <= -len(ring) else (newState - len(ring) if newState > len(ring) else newState)

                tmpMin = min(tmpMin, self.dpHelper(ring, key, steps, dp, startInd + 1, newState) + 1 + abs(step))
            dp[(startInd, state)] = tmpMin
        return dp[(startInd, state)]

    def getSteps(self, ring, keys):
        res = {}
        for k in keys:
            res[k] = []
        for i in range(len(ring)):
            if ring[i] in res:
                if len(ring) - i < i:
                    res[ring[i]].append(i - len(ring))
                else:
                    res[ring[i]].append(i)
        return res


so = Solution()
print so.findRotateSteps("ifrhu", "fhiru")
