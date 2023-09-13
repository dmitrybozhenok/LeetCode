from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image[0])
        n = len(image)
        stack = [(sr, sc)]
        while stack:
            cur = stack.pop()
            cur_color = image[cur[0]][cur[1]]
            if cur_color == color:
                continue
            if cur[0] > 0 and image[cur[0]-1][cur[1]] == cur_color:
                stack.append((cur[0]-1, cur[1]))
            if cur[1] > 0 and image[cur[0]][cur[1]-1] == cur_color:
                stack.append((cur[0], cur[1]-1))
            if cur[0] < n - 1 and image[cur[0]+1][cur[1]] == cur_color:
                stack.append((cur[0]+1, cur[1]))
            if cur[1] < m - 1 and image[cur[0]][cur[1]+1] == cur_color:
                stack.append((cur[0], cur[1]+1))
            image[cur[0]][cur[1]] = color
        return image