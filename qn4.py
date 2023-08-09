#
# Author: Seah Yong Kheng
# Leetcode question 4: Median of Two Sorted Arrays
# 
# Time Complexity: O((n + m) log (n+m))
# Space Complexity: O(n + m)
#
import math 

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined_list = nums1 + nums2
        combined_list.sort()

        def getMedian(aList): 
            middle_index = len(aList) / 2

            if len(aList) % 2 != 0:
                return aList[math.floor(middle_index)]
            left_index = middle_index - 1
            right_index = middle_index
            return (aList[int(left_index)] + aList[int(right_index)]) / 2
        
        if len(nums1) == 0:
            return getMedian(nums2)
        elif len(nums2) == 0:
            return getMedian(nums1)
        else: 
            return getMedian(combined_list)