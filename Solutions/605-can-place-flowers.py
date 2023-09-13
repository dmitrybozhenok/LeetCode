from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev, next = 0, 0
        cur = flowerbed[0]

        for i in range(1,len(flowerbed)):
            cur = flowerbed[i-1]
            next = flowerbed[i]
            if prev == 0 and cur == 0 and next == 0:
                n -= 1
                cur = 1
            prev = cur
        if cur == 0 and next == 0:
            n -= 1

        return n <= 0