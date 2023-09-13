from typing import List


class Solution(object):
    def twoSum(nums: List[int], target: int) -> List[int]:
        seen = {}
        ret = []
        for i in range(len(nums)):
            if seen.keys().__contains__(target - nums[i]):
                ret.append(i)
                ret.append(seen[target - nums[i]])
                return ret
            if nums[i] not in seen:
                seen[nums[i]] = i

        return ret