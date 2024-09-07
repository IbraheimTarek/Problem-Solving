class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] # empty array to store the triplets
        nums.sort() # sorting helps in avoiding duplicate triplets
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: # skip Duplicate Elements
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1 # to decrease the total sum
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j -1] and j < k:
                        j += 1
        return res