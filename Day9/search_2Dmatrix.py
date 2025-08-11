class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
           return False
        m, n = len(matrix), len(matrix[0])        
        top, bottom = 0, m - 1
        while top <= bottom:
            mid_row = (top + bottom) // 2
            if target < matrix[mid_row][0]:
                bottom = mid_row - 1
            elif target > matrix[mid_row][-1]:
                top = mid_row + 1
            else:
                break 
        if not (top <= bottom):
            return False  
        row = (top + bottom) // 2
        left, right = 0, n - 1
        while left <= right:
            mid_col = (left + right) // 2
            if matrix[row][mid_col] == target:
                return True
            elif matrix[row][mid_col] < target:
                left = mid_col + 1
            else:
                right = mid_col - 1
        
        return False