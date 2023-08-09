#
# Author: Seah Yong Kheng
# Leetcode question 3: Longest Substring Without Repeating Characters
# 
# Time Complexity: O(N)
# Space Complexity: O(N)
#
# Notes: Sliding window problem

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        # left window
        left = 0

        result = 0

        # right window
        for r in range(len(s)):
            # when there are duplicates
            while s[r] in char_set:
                # remove until ther eis no more duplicate
                char_set.remove(s[left])
                # add to index
                left += 1
            # add character after removing the old
            char_set.add(s[r])

            result = max(result, r - left + 1)

        return result