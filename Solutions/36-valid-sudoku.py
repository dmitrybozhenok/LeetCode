from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        set = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in range(len(board)):
            horSet = set.copy()
            verSet = set.copy()
            for j in range(len(board[i])):
                if horSet.__contains__(board[i][j]):
                    horSet.remove(board[i][j])
                elif board[i][j] != ".":
                    return False
                if verSet.__contains__(board[j][i]):
                    verSet.remove(board[j][i])
                elif board[j][i] != ".":
                    return False

        for i in range(1, len(board) - 1, 3):
            for j in range(1, len(board) - 1, 3):
                innerSet = set.copy()
                for k in range(i-1, i+2):
                    for s in range(j-1, j+2):
                        if innerSet.__contains__(board[k][s]):
                            innerSet.remove(board[k][s])
                        elif board[k][s] != ".":
                            return False
        return True