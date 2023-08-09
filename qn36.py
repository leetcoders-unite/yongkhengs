#
# Author: Seah Yong Kheng
# Leetcode question 36: Valid Sudoku
# 
# Time Complexity: O(N ^ 2)
# Space Complexity: O(N)
#
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isValidRow(board):
            """Iterates through grid in a row to check for duplicate"""
            for row in board:
                for grid in row:
                    if grid != ".":
                        if row.count(grid) > 1:
                            return False
            return True
        
        def isValidCol(board):
            """Iterates through grid in a row to check for duplicate"""
            for i in range(9):
                temp = []
                for j in range(9):
                    grid_to_check = board[j][i]
                    temp.append(grid_to_check)
                for c in temp:
                    if c != ".":
                        if temp.count(c) > 1:
                            return False
            return True
        
        def isValidSquare(board):
            """Checks surrounding grid"""
            for i in range(1,8,3):  #Middle row of each 3x3 grid
                for j in range(1,8,3): 
                    temp = []
                    center_grid = board[i][j]
                    
                    top_left = board[i-1][j-1]
                    top = board[i-1][j]
                    top_right = board[i-1][j+1]
                    
                    left = board[i][j-1]
                    right = board[i][j+1]
                    
                    bottom_left = board[i+1][j-1]
                    bottom = board[i+1][j]
                    bottom_right = board[i+1][j+1]
                    
                    temp.append(center_grid)

                    temp.append(top_left)
                    temp.append(top)
                    temp.append(top_right)

                    temp.append(left)
                    temp.append(right)

                    temp.append(bottom_left)
                    temp.append(bottom)
                    temp.append(bottom_right)
                    for c in temp:
                        if c != ".":
                            if temp.count(c) > 1:
                                return False
            return True
                    
        
        isValidSquare(board)
        
                    
        #Check the rows
        if isValidRow(board) and isValidCol(board) and isValidSquare(board):
            return True
        return False
            