def threeSum(nums):
    # nums[i] + nums[j] + nums[k] = 0
    # for each triplet, append to the result. Triplets have to be unique.

    # Time: O(n^2)
    # Space: O(1)
    n = len(nums)
    nums.sort()
    res = []
    for i, num in enumerate(nums):
        if i > 0 and num == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            curSum = num + nums[left] + nums[right]
            if curSum == 0:
                res.append([num, nums[left], nums[right]])
                # skip duplicate left values
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # skip duplicate right values
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                # move two pointers to next unique values
                left += 1
                right -= 1
            elif curSum > 0:
                right -= 1
            else:
                left += 1
    return res


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))  # [[-1,-1,2],[-1,0,1]]

nums = [0, 1, 1]
print(threeSum(nums))  # []

nums = [0, 0, 0]
print(threeSum(nums))  # [[0,0,0]]

nums = [-1, 0, 1]
print(threeSum(nums))  # [[-1,0,1]]

nums = [0, 0, 0, 0]
print(threeSum(nums))  # [[0,0,0]]

nums = [1, -1, -1, 0]
print(threeSum(nums))  # [[-1,0,1]]
