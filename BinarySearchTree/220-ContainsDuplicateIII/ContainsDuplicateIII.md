## contains duplicate III

* [leetcode](https://leetcode.com/problems/contains-duplicate-iii/description/)
* @ **Big Number** problem (This is really important!)  —> convert to long type and this needs to reposition numbers to positive.
                            But for python, overflow is not needed to consider at all.

## Solution 1

* @ classic **binary search tree** problem —> using java treeSet with O(k) space

## Solution2

* ​@ bucket  --> each bucket with length t, and will store one element at most(or it will return True directly.)
                The nearest element is in bucket or bucket - 1 or bucket + 1.


