from typing import List
class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
    
solve = Solution()
nums = [2,7,11,15]
print(solve.removeDuplicates(nums))