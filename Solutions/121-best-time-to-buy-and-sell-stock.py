from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        min = prices[0]
        max = prices[0]
        for price in prices:
            if price < min:
                min = price
                max = price
            if price > max:
                max = price
            if max - min > total:
                total = max - min

        return total