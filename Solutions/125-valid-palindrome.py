class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s.lower() if char.isalnum())
        j = 0
        k = len(s)-1
        for i in range(len(s) // 2):
            if s[j] != s[k]:
                return False
            j += 1
            k -= 1
        return True
