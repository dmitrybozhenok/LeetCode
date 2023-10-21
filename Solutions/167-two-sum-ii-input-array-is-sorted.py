from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = 0
        k = len(numbers) - 1
        while True:
            sum = numbers[k] + numbers[j]
            if sum > target:
                k -= 1
            elif sum < target:
                j += 1
            else:
                break
        return [j + 1, k + 1]


solution = Solution()
ret = solution.twoSum([2, 7, 11, 15], 9)
