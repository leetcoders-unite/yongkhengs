#
# Author: Seah Yong Kheng
# Leetcode question 1465: Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
# 
# Time Complexity: O(N)
# Space Complexity: O(N)
#
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:

        # Consider the boundaries
        horizontalCuts.append(h)
        horizontalCuts.append(0)
        verticalCuts.append(w)
        verticalCuts.append(0)

        # sort in ascending order
        horizontalCuts.sort()
        verticalCuts.sort()

        # Minimum area is 1
        maxWidth = 1
        maxHeight = 1

        for i in range(len(horizontalCuts) - 1, -1, -1):
            print(i)
            if horizontalCuts[i] - horizontalCuts[i-1] > maxWidth:
                maxWidth = horizontalCuts[i] - horizontalCuts[i-1]
        
        for i in range(len(verticalCuts) - 1, -1, -1):
            if verticalCuts[i] - verticalCuts[i-1] > maxHeight:
                maxHeight = verticalCuts[i] - verticalCuts[i-1]

        return (maxWidth * maxHeight) % (10**9 + 7)
