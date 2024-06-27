from typing import List
# O(N) solution

class Solution:
    # Two-pass Hash Table
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash and hash[complement] != i:
                return [ i , hash[complement]]
    # one-pass Hash Table
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash:
                return [ i , hash[complement]]
            hash[nums[i]] = i
        
    
solve = Solution()
nums = [2,7,11,15]
print(solve.twoSum(nums,9))