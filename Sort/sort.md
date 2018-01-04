# Overview
* 排序算法可以分为两大类:
    * 比较排序
    * 非比较排序: 要求数据有一定特征，基于数据本身的定位特征，才能不提供比较来确定元素的位置
* 通常，从时间&空间复杂度、稳定性上来比较排序算法。包括计数排序、桶排序、基数排序...

# 比较排序
## Merge Sort
* O(NlogN) & O(N) space
* Stable


## Heap Sort
* O(NlogN) on average (O(N ^ 2) worst)
* Not stable


## Quick Sort
* O(NlogN) time
* Not stable


## Insert Sort
* O(N ^ 2) time
* Stable


## Shell Sort
* O(NlogN)
* Not stable
* 针对 insert sort 的优化：
    * 数据量较小时插入排序速度较快，因为 n 和 n ^ 2 的差距很小
    * 数据基本有序时插入排序效率很高，因为比较和移动的数据量较小
  因此，shell sort的基本思想是将需要排序的序列划分成若干个较小的子序列，对子序列进行插入排序，然后再对基本
  有序的数列进行插入排序，能够提高算法效率。
* 希尔排序的划分子序列不是像归并排序那种的二分，而是采用的叫做**增量**的技术，例如有十个元素的数组进行希尔排序，
首先选择增量为10/2=5，此时第1个元素和第（1+5）个元素配对成子序列使用插入排序进行排序，第2和（2+5）个元素
组成子序列，完成后增量继续减半为2，此时第1个元素、第（1+2）、第（1+4）、第（1+6）、第（1+8）个元素组成子
序列进行插入排序。这种增量选择方法的好处是可以使数组整体均匀有序，尽可能的减少比较和移动的次数，二分法中即使
前一半数据有序，后一半中如果有比较小的数据，还是会造成大量的比较和移动，因此这种增量的方法和插入排序的配合更佳。


# 非比较排序
* 提高比较排序，时间复杂度的下界是O(NlogN)，但是如果可以结合数据本身的特征，通过不比较排序，就能使时间复杂度
降到O(N), 但通常同时会引入一定的空间复杂度。

## Bucket Sort
* split into several buckets and then sort each bucket(can use other sort algorithms, 
or using bucket sort recursively)
* Steps:
    1. **划分**M个桶，then基于某种映射函数将待排序的关键字**映射**到第 i 个桶
    2. 对每个桶中所有元素进行比较排序，然后依次枚举出每个桶中的元素，最后得到一个有序序列。


## Counting Sort
* O(N + k) time & O(k) space, k = max(array[i]) - min(array[i]) + 1
* Stable
* 要求待排序数组的元素都是**整数**。(不要求正数，因为负数可以通过加偏移量)
* 基本思路是通过统计得出每个数字应在的位置
    1. cnt数组统计每个元素的出现次数（数组通过-min做偏移映射） O(N) time & O(k) space
    2. 累加cnt数组得到每个数字的位置 O(k) time
    3. **从后往前**（稳定排序的关键）放置新数组，同时cnt数组相应位置减一  O(N) time


## Radix Sort
* O(d * (n + k)) time & O(k) space, d = 特征个数
* Not stable
* Requirement: All numbers should be negative
* 基本思想是对数据选择多种基数，对每一种基数依次使用桶排序。（也可以看做是一种桶排序，不断地使用不同标准对数据分桶）。
* Steps：
    1. 从个位开始，根据0~9的值将数据分桶；
    2. 将0~9的10个桶中数据按顺序放回到数组中。
    3. 重复该过程一直到最高位。
该方法称为LSD（Least significant digital），还可以从高位到低位，称为MSD。
