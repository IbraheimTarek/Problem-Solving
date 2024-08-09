from typing import List
class Solution():
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if (not stack) or (c == ')' and stack[-1] != '(') or (c == ']' and stack[-1] != '[') or (c == '}' and stack[-1] != '{'):
                    return False
                stack.pop()
        return not stack

solve = Solution()  
s = "()[]{}"
print(solve.isValid(s))

