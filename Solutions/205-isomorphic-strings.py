class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        str_map = {}
        for i in range(len(t)):
            if t[i] in str_map and str_map[t[i]] != s[i]:
                return False
            if t[i] not in str_map:
                if s[i] in str_map.values():
                    return False
                else:
                    str_map[t[i]] = s[i]
        return True