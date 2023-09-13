from collections import deque


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = deque(word1)
        w2 = deque(word2)
        ret = ""
        while w1 or w2:
            if w1:
                ret += w1.popleft()
            if w2:
                ret += w2.popleft()
        return ret