# Merge k Sorted Lists
## Problem Define
* [leetcode](https://leetcode.com/problems/merge-k-sorted-lists/description/)
* A classic problem.

## Solution1
* heap
* Same idea from merge two sorted list: for each round, we select the minimum node   
  and add it to results.
* So the problem convert to how to select the minimum node each round  
  --> here is where heap comes from
  
## Solution2
* DivideAndConquer
* Also the idea from merge two sorted list: for each round, we merge two linked list to one
* This can be implemented using recursion.
