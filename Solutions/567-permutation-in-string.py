class Solution:
    def checkInclusionSlow(self, s1: str, s2: str) -> bool:
        letters = {}
        for s in s1:
            if letters.keys().__contains__(s):
                letters[s] += 1
            else:
                letters[s] = 1

        for i in range(len(s2)):
            if letters.keys().__contains__(s2[i]):
                let = letters.copy()
                for j in range(i, min(i + len(s1), len(s2))):
                    if let.keys().__contains__(s2[j]):
                        let[s2[j]] -= 1
                        if let[s2[j]] == 0:
                            let.pop(s2[j])
                    else:
                        break
                if not let:
                    return True
        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1map, s2map = [0]*26, [0]*26
        for i in range(len(s1)):
            s1map[ord(s1[i]) - ord('a')] += 1
            s2map[ord(s2[i]) - ord('a')] += 1

        matches = 0

        for i in range(26):
            if s1map[i] == s2map[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2map[index] += 1
            if s1map[index] == s2map[index]:
                matches += 1
            elif s1map[index] + 1 == s2map[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2map[index] -= 1
            if s1map[index] == s2map[index]:
                matches += 1
            elif s2map[index] + 1 == s1map[index]:
                matches -= 1
            l += 1
        return matches == 26



solution = Solution()
ret = solution.checkInclusion("ab", "eidbaooo")

