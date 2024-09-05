# For this mock interview, you will go through four phases: Prompt, Plan, Code, & Test.
# Prompt: Understand the problem.
# Plan: Outline your approach.
# Code: Implement your solution.
# Test: Verify your solution works.

# Here is the problem that you will be solving:
# Imagine you have a collection of unique integers labeled 'nums'.
# Your task is to compute all unique arrangements of these integers.
# These arrangements should be returned as a list of lists, where each inner list represents a possible sequence of the given numbers.
 
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
 
# Example 3:
# Input: nums = [1]
# Output: [[1]]
 
# Please note that each integer from 'nums' must appear exactly once in each arrangement, and the input list 'nums' will only contain distinct integers ranging from -10 to 10.
# The length of 'nums' will not exceed 6.

from itertools import permutations

def computeUniqueCombinations(nums):
    # Write your plan below
    #We’ll implement a helper function that will generate permutations by swapping elements.
    #The function will take the current index and the remaining part of the list to generate all permutations.
    #Once we reach the end of the list, we’ll add the current permutation to the result list.
    #The backtracking part involves swapping the elements back to their original positions to explore other possible permutations.
    result = []
    def backtrack(start, end):
        if start == end:
            result.append(nums[:])
        for i in range(start, end):
            nums[start], nums[i] = nums[i], nums[start]  # Swap
            backtrack(start + 1, end)
            nums[start], nums[i] = nums[i], nums[start]  # Backtrack

    backtrack(0, len(nums))
    return result

# Test cases
print(computeUniqueCombinations([1, 2, 3]))  # Example 1
print(computeUniqueCombinations([0, 1]))     # Example 2
print(computeUniqueCombinations([1]))        # Example 3
print(computeUniqueCombinations([]))         # Edge Case 1
print(computeUniqueCombinations([-1, 1]))    # Edge Case 2
