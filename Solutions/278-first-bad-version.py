def isBadVersion(version: int) -> bool:
    return True

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        ret = 0
        while left <= right:
            mid = left + (right - left) // 2
            if not isBadVersion(mid):
                left = mid + 1
                ret = left
            else:
                ret = mid
                right = mid - 1

        return ret