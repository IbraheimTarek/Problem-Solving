
def biggest_diff(nums):
    if nums:
        x1 = min(nums)
        x2 = max(nums)
        return x2-x1
    return 0

print(biggest_diff([10, 3, 5, 6])) # 7
print(biggest_diff([7, 2, 10, 9])) # 8
print(biggest_diff([2, 10, 7, 2])) # 8