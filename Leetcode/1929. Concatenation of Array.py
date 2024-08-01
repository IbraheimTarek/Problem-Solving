from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[i])
        for i in range(len(nums)):
            ans.append(nums[i])
        return ans
    # another solution
    def getConcatenation_V2(self, nums: List[int]) -> List[int]:
        return nums + nums

solve = Solution()
nums = [1,2,1]
print(solve.getConcatenation(nums))