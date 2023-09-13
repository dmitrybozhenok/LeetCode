class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        si = 0
        ti = 0
        while si < len(s) and ti < len(t):
            if t[ti] == s[si]:
                si += 1
            ti += 1
        if si == len(s):
            return True
        return False