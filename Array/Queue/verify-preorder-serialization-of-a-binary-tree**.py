"""
Verify Preorder Serialization of a Binary Tree
@ Queue
@ Corner case: '#' True  & '###' False
"""


class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        chars = preorder.split(',')
        if not chars:
            return True
        queue = [chars[0]]
        ind = 1
        while ind < len(chars):
            if queue:
                queue.pop(0)
                if ind > len(chars) - 2:
                    return False
                if chars[ind] != '#':
                    queue.append(chars[ind])
                ind += 1
                if chars[ind] != '#':
                    queue.append(chars[ind])
                ind += 1
            else:
                return False
        return not queue


so = Solution()
print so.isValidSerialization("9,3,4,#,#,1,#,2,#,6,#,#")
