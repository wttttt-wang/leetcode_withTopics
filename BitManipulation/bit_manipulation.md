# Bit Manipulation
* and, or, not, xor, shift

## ^ tricks
* Use ^ to remove even exactly same numbers and save the odd, 
or save the distinct bits and remove the same.
* Example:
    * Sum of two integers
    ```
    int getSum(int a, int b) {
      return b==0? a:getSum(a^b, (a&b)<<1); //be careful about the terminating condition;
    }
    ```
    * missing number (a xor a = 0)
    ```
    int missingNumber(vector<int>& nums) {
        int ret = 0;
        for(int i = 0; i < nums.size(); ++i) {
            ret ^= i;
            ret ^= nums[i];
        }
        return ret^=nums.size();
    }
    ```

## | tricks
* Keep as many as 1-bits as possible.
* Example:
    * Find the largest power of 2(most significant bit in binary form) which is <= N
    ```
    
    ```