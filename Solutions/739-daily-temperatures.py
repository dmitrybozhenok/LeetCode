from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret = [0]*len(temperatures)
        stack.append(0)
        for t in range(1, len(temperatures)):
            if temperatures[t] <= temperatures[stack[-1]]:
                stack.append(t)
            else:
                while stack and temperatures[t] > temperatures[stack[-1]]:
                    ret[stack[-1]] = t - stack[-1]
                    stack.pop()
                stack.append(t)
        return ret


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
solution = Solution()
result = solution.dailyTemperatures(temperatures)
print("Final result:", result)







