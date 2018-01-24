"""
Number of Boomerangs
@ Hash: O(N ^ 2) time, very easy
"""


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        res = 0
        for i in range(len(points)):
            disMap = {}
            for j in range(len(points)):
                if j == i:
                    continue
                dis = (points[j][1] - points[i][1]) ** 2 + (points[j][0] - points[i][0]) ** 2
                res += disMap.get(dis, 0) * 2
                disMap[dis] = disMap.get(dis, 0) + 1
        return res
