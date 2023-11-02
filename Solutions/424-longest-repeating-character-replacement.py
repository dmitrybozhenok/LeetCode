class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_dic = {}
        res = 0

        l = 0
        maxcount = 0
        for r in range(len(s)):
            count_dic[s[r]] = 1 + count_dic.get(s[r], 0)
            maxcount = max(maxcount, count_dic[s[r]])

            while (r - l + 1) - maxcount > k:
                count_dic[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
            return res