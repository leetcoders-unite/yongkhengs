/**
 * Author: Seah Yong Kheng
 * Leetcode question 1672: Richest Customer Wealth
 * 
 * Time Complexity: O(N^2)
 * Space Complexity: O(1)
 */
class Solution {
    public int maximumWealth(int[][] accounts) {
        int highestWealth = 0;
        
        for (int i = 0; i < accounts.length; i++) {
            int currentWealth = 0;
            for (int j = 0; j < accounts[i].length; j++) {
                currentWealth += accounts[i][j];
            }
            if (currentWealth > highestWealth) {
                highestWealth = currentWealth;
            }
        }
        return highestWealth;
    }
}