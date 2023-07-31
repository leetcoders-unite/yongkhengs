#
# Author: Seah Yong Kheng
# Leetcode question 1: Two Sum
# 
# Time Complexity: O(N)
# Space Complexity: O(N)
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums) - 1):
            # Get the current value
            temp = nums.pop(i)
            remainder = target - temp
            if remainder in nums:
                # Determine if the remainder is in list ( + 1 cause 1 element is popped)
                res.append(nums.index(remainder) + 1)
                #Inserts back
                nums.insert(i, temp)
                res.append(i)
                break
            else:
                # Inserts back element and clears array if not in array
                nums.insert(i, temp)
                res = []
        return res

