class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for symbol in s:
            if symbol in dic:
                dic[symbol] += 1
            else:
                dic[symbol] = 1
        for symbol in t:
            if symbol in dic:
                dic[symbol] -= 1
            else:
                return False
        return all(value == 0 for value in dic.values())