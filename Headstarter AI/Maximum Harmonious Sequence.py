from collections import Counter

def findLargestHarmoniousSubsequence(nums):
    freq = Counter(nums)
    max_length = 0
    for num in nums:

        if num + 1 in nums:
            current_freq = freq[num] + freq[num + 1]
            max_length = max(max_length, current_freq)
    
    return max_length



print(findLargestHarmoniousSubsequence([1,3,2,2,5,2,3,7]))  # Output: 5
print(findLargestHarmoniousSubsequence([1,2,3,4]))  # Output: 2
print(findLargestHarmoniousSubsequence([1,1,1,1])) # 0