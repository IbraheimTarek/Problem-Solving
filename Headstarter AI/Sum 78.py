def sum78(nums):
    ignore = False
    total = 0
    for n in nums:
        if n == 7:
            ignore = True
        elif n==8 and ignore:
            ignore = False
        elif not ignore:
            total += n
    return total

print(sum78([1, 2, 2]))  # Output: 5
print(sum78([1, 2, 2, 7, 99, 99, 8]))  # Output: 5
print(sum78([1, 1, 7, 8, 2]))  # Output: 4