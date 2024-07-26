from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = len(nums)
        j = 0
        for i in range(0, l):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

solve = Solution()
nums = [2,7,2,15]
print(solve.removeElement(nums,2))