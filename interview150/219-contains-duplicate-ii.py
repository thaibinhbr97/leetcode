def containsNearbyDuplicate(nums, k):
    # method 1:
    # using sliding window to keep track of the "valid" window k in nums and use seen set to keep track of existing
    # numbers
    # time: O(n)
    # space: O(k)
    # seen = set()
    # left = 0
    # for right in range(len(nums)):
    #     if right - left > k:
    #         seen.remove(nums[left])
    #         left += 1
    #     if nums[right] in seen:
    #         return True
    #     seen.add(nums[right])
    # return False

    # method 2:
    # using a dictionary to keep track of indexes. If the difference between a current index and a previous index is smaller
    # or equal to k, return True. Otherwise, return False after traversing through nums
    # time: O(n)
    # space: O(n)
    index_map = {}
    for i, num in enumerate(nums):
        # if num exists in index_map, check the difference
        if num in index_map:
            if abs(i - index_map[num]) <= k:
                return True
        # needs to update the current num's index in index_map
        index_map[num] = i
    return False


nums = [1, 2, 3, 1]
k = 3
print(containsNearbyDuplicate(nums, k))  # true


nums = [1, 0, 1, 1]
k = 1
print(containsNearbyDuplicate(nums, k))  # true

nums = [1, 2, 3, 1, 2, 3]
k = 2
print(containsNearbyDuplicate(nums, k))  # false

nums = [99, 99]
k = 2
print(containsNearbyDuplicate(nums, k))  # true

nums = [0, 1, 2, 3, 2, 5]
k = 3
print(containsNearbyDuplicate(nums, k))  # true
