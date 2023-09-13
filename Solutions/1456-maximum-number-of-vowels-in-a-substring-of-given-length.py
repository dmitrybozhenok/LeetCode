class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def isVowel(s) -> bool:
            vowels = ['a', 'e', 'i', 'o', 'u']
            return s.lower() in vowels
        sl = list(s)
        cur = 0
        for i in range(k):
            if isVowel(sl[i]):
                cur += 1
        max = cur
        for i in range(k, len(sl)):
            if isVowel(sl[i]):
                cur += 1
            if isVowel(sl[i - k]):
                cur -= 1
            if max < cur:
                max = cur
        return max