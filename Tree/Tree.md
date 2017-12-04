# Binary Search Tree
* Elements in left tree are all smaller than parent, elements in right tree are all bigger than parent.
* Generally O(logN) time, but time complexity will increase to O(N) when BST is not balanced.
* Using java TreeMap/TreeSet which is red-black tree(balanced) to ensure O(logN) update & search.

# Segment Tree
* Widely used in **consecutive intervals dynamic search** problem.
* Segment is a balanced binary tree(complete binary tree). So each operation is with O(logN) time.
* Each node in segment tree is an interval.
* The main point is the way it split the interval:   
  `if parent=[a, b], then leftChild=[a,(a+b)/2], rightChild=[(a+b)/2 + 1, b]`

# Binary Indexed Tree
* O(logN) update single element & sum prefix.
* element with index i manage origin array's elements of interval [i - 2k + 1, i] (inclusive). 

# Comparison
## BIT V.S. Segment Tree
* Their common function is to **maintain interval info** and support **single element modification**   
  both in O(logN) time.
* And the operator must satisfy **associative law** such as add/multiply/max/min.
* Generally speaking, segment tree can maintain arbitrary interval, but **BIT can only maintain prefix info**.
    * I say in 'generally' because in some case, BIT does support some 'interval' info.   
    This happens when the operation exists 'inverse element'.    
    That's to say when we get twice prefix, and operate with the first prefix then we get the result.   
    You may have already seen this in 'BinaryIndexedTree/count-of-range-sum'
    * For example: when we use BIT to deal with sum operator, we can maintain all interval sum   
    by getting prefix sum twice and subtract the former one.    
    But for max/min operator, 'inverse element' not exists, so we cannot use BIT to maintain all interval info.
* Segment Tree over BIT: support interval, so can provide wider range of use.   
                         (Problems can solved by BIT can also be solved by BIT.)
* BIT over Segment Tree: BIT use bit manipulation, so can provide with **lower constant complexity**.

# Exercises
* BIT, Segment Tree, DivideAndConquer(Merge Sort):
    * count-of-range-sum
    * count-of-smaller-numbers-after-self
    * Reverse pairs