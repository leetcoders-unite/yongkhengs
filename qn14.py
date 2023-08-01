#
# Author: Seah Yong Kheng
# Leetcode question 14: Longest Common Prefix
# 
# Time Complexity: O(N)
# Space Complexity: O(1)
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # will be present in all subsequent words
        prefix = strs[0]

        for word in strs[1:]:
            # iterating through the strs list
            i = 0
            # i is lesser than original word
            # i is lesser than length of current word
            # original word[i] is same as current word[i] (positioning)
            while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
                i += 1

            # remove unncessary characters not found
            prefix = prefix[:i]

        return prefix



        