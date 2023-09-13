from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ret = []
        greatest = max(candies)
        for kid in candies:
            if kid + extraCandies < greatest:
                ret.append(False)
            else:
                ret.append(True)
        return ret