import java.util.TreeSet;

/**
 * Contains Duplicate III
 *
 * Explanation: Given a constraint on the range of the values of the elements to be considered duplicates.
 *              So we can do a range check which can be implemented in a 'tree' which takes O(logN) for balanced tree.
 *              Here we can use TreeSet which maintain an O(k) space BST and takes O(Nlogk) time.
 *
 * Corner case: big number. (nums[i] + t) may overflow. --> We can use long type to store, 
 *              but in case of negative number, we 'reposition every element to start from Integer.MIN_VALUE'
 */
public class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if (nums == null || nums.length == 0 || k < 0) return false;
        TreeSet<Long> bst = new TreeSet<>();

        for (int i = 0; i < nums.length; i++) {
            long mappedVal = (long)nums[i] - Integer.MIN_VALUE;

            // find v that mappedVal - t <= v <= mappedVal + t
            Long ceil = bst.ceiling(mappedVal - (long)t);
            Long floor = bst.floor(mappedVal + (long)t);
            // check ceil <= mappedVal  & floor >= mappedVal is important!
            if ((ceil != null && ceil <= mappedVal) || (floor != null && floor >= mappedVal)) return true;

            bst.add(mappedVal);

            // remove i - k
            if (i >= k) {
                long removal = (long) nums[i - k] - Integer.MIN_VALUE;
                bst.remove(removal);
            }
        }

        return false;
    }
}


