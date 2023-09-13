class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        numbers = [0, 1]
        for i in range(2, n + 1):
            numbers.append(numbers[i-1] + numbers[i-2])
        return numbers[n]