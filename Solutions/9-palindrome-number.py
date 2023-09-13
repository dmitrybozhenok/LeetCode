class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        intStr = str(x)
        stack = []
        for c in intStr:
            stack.append(c)
        for c in intStr:
            if (stack.pop() != c):
                return False
        return True