def findPeakElement(nums):
    # a peak element is an element that is strictly greater than its neighbor
    # example 1: 1 2 3 1 -> 2
    # example 2: 1 2 1 3 5 6 4
    """
    if curr is smaller than next, it means that the peak appears on the right of curr
    if curr is larger than next, it means that the peak is on the left of curr, or curr
    1 2 3 1
    left = mid + 1 = 3 -> left == right -> break
    right = mid = 3
    mid = (left + right) // 2 = 2
    compare nums[mid] and nums[mid+1]
    nums[mid] = 3
    nums[mid+1] = 1
    2 < 3 -> peak on the right of curr -> binary search on the right of curr
    3 > 1 -> peak on the left of curr or curr -> binary search on the left of curr or curr
    """
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left


nums = [1, 2, 3, 1]
print(findPeakElement(nums))  # 2

nums = [1, 2, 1, 3, 5, 6, 4]
print(findPeakElement(nums))  # 5
