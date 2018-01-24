/**
 * Find Right Interval
 * @ Binary Search Tree (Binary Search): Please be familiar with the usage of java 'TreeMap'.
 */
/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
class Solution {
    public int[] findRightInterval(Interval[] intervals) {
        int[] results = new int[intervals.length];
        TreeMap<Integer, Integer> treeMap = new TreeMap<>();
        for (int i = 0; i < intervals.length; i++) treeMap.put(intervals[i].start, i);
        for (int i = 0; i < intervals.length; i++) {
            Map.Entry<Integer, Integer> entry = treeMap.ceilingEntry(intervals[i].end);
            results[i] = (entry != null) ? entry.getValue() : -1;
        }
        return results;
    }
}

