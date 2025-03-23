def canJump(nums):
    # Time: O(n), n is length of nums
    # Space: O(1)
    max_reach = 0
    n = len(nums)
    for i, jump in enumerate(nums):
        if i > max_reach:  # there is no way to jump from max_reach to the end
            return False
        max_reach = max(max_reach, i + jump)
        if max_reach >= n - 1:  # return True if jump at least reaches the end of nums
            return True
    return True


nums = [2, 3, 1, 1, 4]
print(canJump(nums))  # True

nums = [2, 2, 1, 1, 4]
print(canJump(nums))  # True

nums = [2, 5, 1, 1, 4]
print(canJump(nums))  # True

nums = [3, 2, 1, 0, 4]
print(canJump(nums))  # False
