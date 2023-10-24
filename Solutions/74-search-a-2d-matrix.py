from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix) - 1
        m = len(matrix[0]) - 1
        top, bottom = n, 0
        left, right = 0, m
        while bottom <= top:
            mid_v = bottom + (top - bottom) // 2
            if target > matrix[mid_v][m]:
                bottom = mid_v + 1
            elif target < matrix[mid_v][0]:
                top = mid_v - 1
            else:
                while left <= right:
                    mid_h = left + (right - left) // 2
                    if target > matrix[mid_v][mid_h]:
                        left = mid_h + 1
                    elif target < matrix[mid_v][mid_h]:
                        right = mid_h - 1
                    else:
                        return True
                return False
        return False


solution = Solution()
ret = solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)
