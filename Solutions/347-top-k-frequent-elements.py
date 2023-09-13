from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen.keys():
                seen[num] += 1
            else:
                seen[num] = 0
        sortedSeen = sorted(seen.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sortedSeen[:k]]