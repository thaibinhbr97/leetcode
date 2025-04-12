def longestConsecutive(nums):
    # approach 1: sorting
    # time: O(nlogn)
    # space: O(n)
    # sort nums and use two pointers to keep track of consecutive elements and update maxSoFar when right pointer
    # is not consecutive
    # if not nums:
    #     return 0
    # nums = sorted(set(nums))
    # left = 0
    # right = 1
    # maxSoFar = 0
    # while right < len(nums):
    #     if nums[right] == nums[right - 1] + 1:  # if it is an increasing sequence
    #         right += 1
    #     else:
    #         maxSoFar = max(maxSoFar, right - left)
    #         left = right
    #         right += 1
    # maxSoFar = max(maxSoFar, right - left)
    # return maxSoFar

    # approach 2:
    # time: O(n)
    # space: O(n)
    # use dictionary/hashmap to keep track existing number from nums -> by traversing 1 time through nums
    # if not nums:
    #     return 0
    # maxSoFar = 0
    # distinct_nums = set(nums)
    # startSequence = {}
    # for num in distinct_nums:
    #     startSequence[num] = 0
    # for num in distinct_nums:
    #     if num - 1 not in startSequence:
    #         startSequence[num] = 1
    # for num in distinct_nums:
    #     if startSequence[num] == 1:
    #         temp = 1
    #         while num + 1 in startSequence:
    #             temp += 1
    #             num += 1
    #         maxSoFar = max(maxSoFar, temp)
    # return maxSoFar

    # approach 3: using set
    # time: O(n)
    # space: O(n)
    if not nums:
        return 0
    distinct_nums = set(nums)
    maxSoFar = 0
    for num in distinct_nums:
        if num - 1 not in distinct_nums:
            temp = 1
            while num + temp in distinct_nums:
                temp += 1
            maxSoFar = max(maxSoFar, temp)
    return maxSoFar


nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))  # 4

nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(longestConsecutive(nums))  # 9

nums = [1, 0, 1, 2]
print(longestConsecutive(nums))  # 3

nums = [0, -1]
print(longestConsecutive(nums))  # 2
