from typing import List
class Solution():
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "C":
                stack.pop()
            else:
                 stack.append(int(op))
        return sum(stack)

solve = Solution()
ops = ["5","-2","4","C","D","9","+","+"]
print(solve.calPoints(ops))
