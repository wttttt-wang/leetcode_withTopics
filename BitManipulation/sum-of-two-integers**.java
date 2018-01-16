/**
** Sum of Two Integers
** @ Bit Manipulation
** @ Note that not use python for <<.  = =
**/


class Solution {
    public int getSum(int a, int b) {
        return b==0? a : getSum(a ^ b, (a & b) << 1);
    }
}