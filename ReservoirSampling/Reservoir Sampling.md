# Reservoir Sampling
1. Problem Define:
   Choose k entries from n numbers. Make sure each number is selected with the probability of k/n.

2. Basic Idea:
   1. Choose 1, 2, 3, ..., k first and put them into the reservoir.
   2. For k + 1, pick it with probability of k/(k + 1), and randomly replace a number in the reservoir.
   3. For k + i, pick it with probability of k/(k + i), and randomly replace a number in the reservoir.
   4. Repeat until k + i reaches n.

3. Proof:
   1. For k + i, the probability that it is selected and will replace a number in the reservoir is k/(k + i)
   2. For a number in the reservoir before(let's say X), the probability that it keeps in staying in the reservoir is
      * P(X was in the reservoir last time) * P(X is not replaced by k + i)
      * = k / (k + i - 1) * (1 - k / (k + i) * 1 / k)  --> k / (k + i - 1) because of same probability of all elements in the reservoir.
      * = k / (k + i)
   3. When k + i reaches n, the probability of each number staying in the reservoir is k/n.

3. 应用场景：
   给定一个数据流，**数据流长度很大or未知**。并且对该数据流中数据只能访问一次。请给出一个随机选择算法，使得数据流中所有数据被选中的概率相等。
   一个很棒的链接: http://blog.jobbole.com/42550/
