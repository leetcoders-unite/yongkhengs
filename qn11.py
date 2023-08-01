#
# Author: Seah Yong Kheng
# Leetcode question 11: Container with most water
# 
# Time Complexity: O(N)
# Space Complexity: O(1)
#
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        # if this is false, means the 2 walls went through each other
        while left < right:
            # difference in index
            current_width = right - left
            # water will overflow if we do not take the min height
            current_height = min(height[left], height[right])
            # replace result with the new highest area
            max_area = max(current_width * current_height, max_area)

            
            if height[left] < height[right]:
                # if left wall is lower than right wall, stay at right wall and move left wall inwards
                left += 1
            else:# if right wall is lower than left wall, stay at left wall and move right wall inwards
                right -= 1

        return max_area