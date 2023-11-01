class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        i, k = 0, 0
        ret = 0
        while i < len(s) and k < len(s):
            map[s[i]] = i
            k = i + 1
            while k < len(s):
                if map.keys().__contains__(s[k]):
                    i = map[s[k]] + 1
                    ret = max(ret, len(map))
                    map = {}
                    break
                else:
                    map[s[k]] = k
                    k += 1
        ret = max(ret, len(map))
        return ret

solution = Solution()
ret = solution.lengthOfLongestSubstring("abcabcbb")