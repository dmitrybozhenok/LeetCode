class Solution:
    def reverseWords(self, s: str) -> str:
        st = list(s)
        words = []
        i = 0
        len1 = len(st)
        while i < len1:
            if st[i] != ' ':
                k = i
                while True:
                    k += 1
                    if k == len1 or st[k] == ' ':
                        words.append(''.join(st[i:k]))
                        i = k
                        break
            i += 1
        words.reverse()
        return " ".join(words)