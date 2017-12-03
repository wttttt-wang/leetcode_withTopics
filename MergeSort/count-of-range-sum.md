# Count of range sum
## Problem Define
* [leetcode](https://leetcode.com/problems/count-of-range-sum/description/)
1. for range sum --> use prefix sum. 
2. Then the problem convert to: given an array, find count of pairs where `lower <= arr[i] - arr[j] <= upper`
3. Then the most straightforward solution is to compute diff of each pair and check. This is O(N ^ 2) time.

## Solution1
* Divide And Conquer (Merge Sort)
* Explanation: count the pairs of left & right part separately, and sort them in the meanwhile.
               then count the intersect pairs which satisfy the requirement. 
               (Intersect means select one from left and the other from right)
               As left & right are already sorted, use two pointers to count. And merge sort this two array.

## Solution2
* Binary Indexed Tree
* Explanation: For prefixSum to find `lower <= sum[j] - sum[i - 1] <= upper` is to 
               find `lower + sum[i - 1] <= sum[j] <= upper + sum[i - 1]`
* Note: Pay attention to the process of discretization.

## Solution3
* Segment Tree
