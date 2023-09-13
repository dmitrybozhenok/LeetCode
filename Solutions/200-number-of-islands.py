from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        m = len(grid[0])
        n = len(grid)
        stack = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '0':
                    continue
                else:
                    num += 1
                    stack.append((i, j))
                    while stack:
                        cur = stack.pop()
                        cur_state = grid[cur[0]][cur[1]]
                        if cur_state == '0':
                            continue
                        grid[cur[0]][cur[1]] = '0'
                        if cur[0] > 0 and grid[cur[0] - 1][cur[1]] == '1':
                            stack.append((cur[0] - 1, cur[1]))
                        if cur[1] > 0 and grid[cur[0]][cur[1] - 1] == '1':
                            stack.append((cur[0], cur[1] - 1))
                        if cur[0] < n - 1 and grid[cur[0] + 1][cur[1]] == '1':
                            stack.append((cur[0] + 1, cur[1]))
                        if cur[1] < m - 1 and grid[cur[0]][cur[1] + 1] == '1':
                            stack.append((cur[0], cur[1] + 1))
        return num