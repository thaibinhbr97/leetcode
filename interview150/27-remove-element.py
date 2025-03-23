def removeElement(nums, val):
    # Time: O(n), n is length of nums
    # Space: O(1) for using two pointers and modify nums in-place
    left = 0  # pointer for valid elements
    for right in range(len(nums)):
        if nums[right] != val:  # if current element is not 'val'
            nums[left] = nums[right]  # move it to the valid position
            left += 1  # increment pointer for valid elements
    return left  # number of valid elements


nums = [3, 2, 2, 3]
val = 3
print(removeElement(nums, val))  # 2, nums = [2,2,_,_]

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(removeElement(nums, val))  # 5, nums = [0,1,4,0,3,_,_,_]

nums = [2]
val = 3
print(removeElement(nums, val))  # 1, nums = [2]
