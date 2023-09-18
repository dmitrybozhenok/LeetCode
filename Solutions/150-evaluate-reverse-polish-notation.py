from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }
        for token in tokens:
            if token not in ('+', '-', '/', '*'):
                stack.append(token)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(operators[token](a, b))
        return int(stack.pop())

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b