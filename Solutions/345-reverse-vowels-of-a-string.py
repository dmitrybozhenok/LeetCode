class Solution:
    def reverseVowels(self, s: str) -> str:
        sa = list(s)
        vowels = []


        def isVowel(s: str):
            vowels = ['a', 'e', 'i', 'o', 'u']
            if vowels.__contains__(s.lower()):
                return True
            return False


        for i in range(len(sa)):
            if isVowel(sa[i]):
                vowels.append(sa[i])
        for i in range(len(sa)):
            if isVowel(sa[i]):
                sa[i] = vowels.pop()
        return ''.join(sa)