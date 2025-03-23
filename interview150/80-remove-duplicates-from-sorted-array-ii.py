def removeDuplicates(nums):
    # Time: O(n), n is length of nums
    # Space: O(1)
    left = 1  # start from the second element
    for right in range(2, len(nums)):
        if nums[left - 1] != nums[right]:
            left += 1
            nums[left] = nums[right]
    return left + 1  # length of valid elements


nums = [1, 1, 1, 2, 2, 3]
print(removeDuplicates(nums))  # 5, nums = [1,1,2,2,3,_]

nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(removeDuplicates(nums))  # 7, nums = [0,0,1,1,2,3,3,_,_]
