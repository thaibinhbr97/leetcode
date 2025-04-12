def containsDuplicate(nums):
    # using set
    # Time: O(n)
    # Space: O(n)
    seen = set()
    for num in nums:
        if num not in seen:
            seen.add(num)
        else:
            return True
    return False

    # sorting
    # time: O(nlogn)
    # space: O(1)
    # nums.sort()
    # for i in range(1, len(nums)):
    #     if nums[i] == nums[i - 1]:
    #         return True
    # return False


nums = [1, 2, 3, 1]
print(containsDuplicate(nums))  # true

nums = [1, 2, 3, 4]
print(containsDuplicate(nums))  # false

nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(containsDuplicate(nums))  # true
