/**
 * Author: Seah Yong Kheng
 * Leetcode question 1672: Richest Customer Wealth
 * 
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
class Solution {
    public int numberOfSteps(int num) {
        int stepCount = 0;
        while (num != 0) {
            if (num % 2 == 0) {
                // Even
                num = num / 2;
                stepCount ++;
            } else if (num % 2 == 1) {
                // Odd
                num = num - 1;
                stepCount ++;
            }
        }
        return stepCount;
    }
}