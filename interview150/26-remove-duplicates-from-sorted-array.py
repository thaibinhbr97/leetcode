def removeDuplicates(nums):
    """
    given integer array nums sorted in non-decreasing order, remove the duplicates in-place on the array such that each unique element appears
    only once. The relative order of elements in the array should be kept the same.
    """
    # Time: O(n), n: length of nums since we traverse nums once
    # Space: O(1) since we only use 2 pointers
    left = 0  # pointer for unique elements
    for right in range(1, len(nums)):
        if nums[left] != nums[right]:  # found a new unique element
            left += 1  # move unique pointer
            nums[left] = nums[
                right
            ]  # copy a new unique element on the position of left
    return left + 1  # length of unique elements


nums = [1, 1, 2]
print(removeDuplicates(nums))  # 2, nums = [1,2,_]

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums))  # 5, nums = [0,1,3,4,5,_,_,_,_,_]
