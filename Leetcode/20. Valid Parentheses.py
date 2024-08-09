from typing import List
class Solution():
    def isValid(self, s: str) -> bool:
        for i in range(len(s) - 1):
            if s[i] == '(' and s[i + 1] != ')':
                return False
            elif s[i] == '[' and s[i + 1] != ']':
                return False
            elif s[i] == '{' and s[i + 1] != '}':
                return False
            i += 1
        return True

solve = Solution()  
s = "(]"
print(solve.isValid(s))

