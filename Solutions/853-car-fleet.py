from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p,s in zip(position, speed)]
        stack = []
        for p, s in sorted(pairs)[::-1]:
            eta = (target-p)/s
            if not stack:
                stack.append(eta)
            else:
                if eta > stack[-1]:
                    stack.append(eta)
        return len(stack)