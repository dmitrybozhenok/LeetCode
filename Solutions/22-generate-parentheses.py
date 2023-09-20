from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(opens, closes):
            if opens == closes == n:
                res.append("".join(stack))
                return

            if opens < n:
                stack.append("(")
                backtrack(opens + 1, closes)
                stack.pop()

            if closes < opens:
                stack.append(")")
                backtrack(opens, closes + 1)
                stack.pop()

        backtrack(0, 0)
        return res
