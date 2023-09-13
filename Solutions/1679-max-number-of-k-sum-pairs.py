from collections import Counter
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        res = 0
        seen = set()
        for x in c:
            rem = k - x
            if x not in seen and rem in c:

                if x == rem:
                    res += c[x] // 2
                else:
                    res += min(c[x], c[rem])
                seen.add(x)
                seen.add(rem)
        return res