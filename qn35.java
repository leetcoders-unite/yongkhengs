/**
 * Author: Seah Yong Kheng
 * Leetcode question 35: Search Insert Position
 *
 * Time Complexity: O(log N)
 * Space Complexity: O(1)
 */
public class Solution {
    public int searchInsert(int[] nums, int target) {
        // Binary search
        int left = 0;
        int right = nums.length - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
}