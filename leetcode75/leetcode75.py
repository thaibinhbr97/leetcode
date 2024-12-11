# ARRAY/STRING

# LEETCODE 151
# def reverseWords(s):
#     # O(n) for time, O(n) for space
#     low = s.split() # list of words
#     res = []
#     n = len(low)
#     for i in range(n-1, -1, -1):
#         res.append(low[i])

#     return ' '.join(res)

# s = "the sky is blue"
# print(reverseWords(s)) # "blue is sky the"

# s = "  hello world  "
# print(reverseWords(s)) # "world hello"

# s = "a good   example"
# print(reverseWords(s)) # "example good a"

# LEETCODE 238
# def productExceptSelf(nums):
#     # # O(n) for time, O(n) for space
#     # n = len(nums)
#     # left = []
#     # right = [0]*(n-1)
#     # result = []
#     # # calculate the prefix product of each ith element
#     # for i in range(len(nums)):
#     #     if i == 0:
#     #         left.append(1)
#     #     else:
#     #         left.append(left[i-1]*nums[i-1])
#     # # print(left)

#     # # calculate the suffix product of each ith element
#     # for j in range(len(nums)-1, -1, -1):
#     #     if j == len(nums) - 1:
#     #         right.append(1)
#     #     else:
#     #         right[j] = right[j+1]*nums[j+1]
#     # # print(right)

#     # # construct the result by mutiplying all elements in the prefix and suffix array
#     # k = 0
#     # while k < len(left):
#     #     result.append(left[k]*right[k])
#     #     k += 1

#     # return result


#     # O(n) for time, O(1) for space since output array ans does not count as extra space for space complexity analysis
#     ans = []
#     for i in range(len(nums)):
#         if i == 0:
#             ans.append(1)
#         else:
#             ans.append(ans[i-1]*nums[i-1])

#     for j in range(len(nums)-1, -1,-1):
#         if j == len(nums) -1:
#             suffix = 1
#         else:
#             suffix *= nums[j+1]
#             ans[j] = ans[j]*suffix

#     return ans


# nums = [1,2,3,4]
# print(productExceptSelf(nums)) # [24,12,8,6]

# nums = [-1,1,0,-3,3]
# print(productExceptSelf(nums)) # [0,0,9,0,0]

# LEETCODE 334
# def increasingTriplet(nums):
#     # O(n) for time, O(1) for space
#     first_num = float("inf")
#     second_num = float("inf")

#     for n in nums:
#         if n <= first_num:
#             first_num = n
#         elif n <= second_num:
#             second_num = n
#         else:
#             return True
#     return False


# nums = [1, 2, 3, 4, 5]
# print(increasingTriplet(nums))  # true

# nums = [5, 4, 3, 2, 1]
# print(increasingTriplet(nums))  # false

# nums = [2, 1, 5, 0, 4, 6]
# print(increasingTriplet(nums))  # true

# nums = [20, 100, 10, 12, 5, 13]
# print(increasingTriplet(nums))  # true

# nums = [1, 5, 0, 4, 1, 3]
# print(increasingTriplet(nums))  # true

# LEETCODE 443
# def compress(chars):
#     # # O(n) for time, O(n) for space
#     # n = len(chars)
#     # s = chars[0]
#     # count = 1
#     # for i in range(1, n):
#     #     if chars[i] == chars[i - 1]:
#     #         count += 1
#     #     else:
#     #         if count != 1:
#     #             s += str(count)
#     #         s += chars[i]
#     #         count = 1
#     # if count > 1:
#     #     s += str(count)
#     # for i in range(len(s)):
#     #     chars[i] = s[i]
#     # chars = chars[: i + 1]
#     # return len(chars)

#     # # Online solution
#     # # O(n) for time, O(1) for space
#     # i = 0
#     # res = 0
#     # while i < len(chars):
#     #     group_length = 1
#     #     while i + group_length < len(chars) and chars[i + group_length] == chars[i]:
#     #         group_length += 1
#     #     chars[res] = chars[i]
#     #     res += 1
#     #     if group_length > 1:
#     #         str_repr = str(group_length)
#     #         chars[res : res + len(str_repr)] = list(str_repr)
#     #         res += len(str_repr)
#     #     i += group_length
#     # return res

#     # O(n) for time, O(1) for space
#     # 2 pointers
#     i = 0  # keep track of a unique letter
#     index = 0
#     while i < len(chars):
#         j = i  # keep track of a number of times a letter appears
#         while j < len(chars) and chars[j] == chars[i]:
#             j += 1

#         chars[index] = chars[i]
#         index += 1

#         if j - i > 1:
#             count = str(j - i)
#             for c in count:
#                 chars[index] = c
#                 index += 1

#         i = j
#     # print(chars)
#     return index


# chars = ["a", "a", "b", "b", "c", "c", "c"]
# print(compress(chars))  # 6 "a2b2c3"

# chars = ["a"]
# print(compress(chars))  # 1 "a"

# chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
# print(compress(chars))  # 4 ["a","b","1","2"]

# chars = ["a", "a", "a", "b", "b", "a", "a"]
# print(compress(chars))  # 6 ["a","3","b","2","a","2"]


# TWO POINTERS


# LEETCODE 283
# def moveZeros(nums):
#     # # O(n) for time, O(1) for space
#     # for num in nums:
#     #     if num == 0:
#     #         nums.remove(0) # O(n) for time
#     #         nums.append(0)
#     # print(nums)

#     # O(n) for time, O(1) for space
#     # Two pointers
#     i = 0
#     j = 1
#     while j < len(nums):
#         if nums[i] == 0:
#             if nums[j] != 0:
#                 # do the swap
#                 temp = nums[j]
#                 nums[j] = 0
#                 nums[i] = temp
#                 i += 1
#             j += 1
#         else:
#             i += 1
#             j += 1
#     print(nums)


# nums = [0, 1, 0, 3, 12]
# print(moveZeros(nums))  # [1,3,12,0,0]

# nums = [0]
# print(moveZeros(nums))  # [0]

# nums = [1, 0]
# print(moveZeros(nums))  # [1,0]


# LEETCODE 392
# import bisect
# from collections import defaultdict


# def isSubsequence(s, t):
#     # # Two pointers
#     # # O(n+m) for tine, O(1) for space
#     # LEFT_BOUND = len(s)
#     # RIGHT_BOUND = len(t)
#     # left = 0
#     # right = 0
#     # while left < LEFT_BOUND and right < RIGHT_BOUND:
#     #     # move both pointers or just the right pointer
#     #     if s[left] == t[right]:
#     #         left += 1
#     #     right += 1
#     # return left == LEFT_BOUND

#     letter_indices_table = defaultdict(list)
#     for index, letter in enumerate(t):
#         letter_indices_table[letter].append(index)

#     curr_match_index = -1
#     for letter in s:
#         if letter not in letter_indices_table:
#             return False  # no match at all, early exit

#         # greedy match with binary search
#         indices_list = letter_indices_table[letter]
#         match_index = bisect.bisect_right(indices_list, curr_match_index)
#         if match_index != len(indices_list):
#             curr_match_index = indices_list[match_index]
#         else:
#             return False  # no suitable match found, early exit

#     return True


# s = "abc"
# t = "ahbgdc"
# print(isSubsequence(s, t))  # true

# s = "axc"
# t = "ahbgdc"
# print(isSubsequence(s, t))  # false

# s = "abcd"
# t = "ab"
# print(isSubsequence(s, t))  # false


# LEETCODE 11
# def maxArea(height):
#     # # Greedy
#     # # O(n^2) for time
#     # ans = 0
#     # for i in range(len(height)):
#     #     for j in range(i + 1, len(height)):
#     #         area = (j - i) * min(height[i], height[j])
#     #         ans = max(ans, area)
#     # return ans

#     # Two pointers
#     left = 0
#     right = len(height) - 1
#     ans = 0
#     while left < right:
#         area = (right - left) * min(height[left], height[right])
#         ans = max(ans, area)
#         if height[left] <= height[right]:
#             left += 1
#         else:
#             right -= 1
#     return ans


# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# print(maxArea(height))  # 49

# height = [1, 1]
# print(maxArea(height))  # 1

# # LEETCODE 1679
# from collections import Counter


# def maxOperations(nums, k):
#     # # Two pointers
#     # # O(nlogn) for time, O(1) for space
#     # ans = 0
#     # left = 0
#     # right = len(nums) - 1
#     # nums.sort()
#     # print(nums)
#     # while left < right:
#     #     lv = nums[left]
#     #     rv = nums[right]
#     #     total = lv + rv
#     #     if total == k:
#     #         ans += 1
#     #         left += 1
#     #         right -= 1
#     #     elif total > k:
#     #         right -= 1
#     #     else:
#     #         left += 1

#     # return ans

#     # Hash Table
#     # O(n) for time, O(n) for space
#     c = Counter(nums)
#     count = 0
#     seen = set()

#     for x in c:
#         if x not in seen and k - x in c:
#             if x == k - x:
#                 count += c[x] // 2
#             else:
#                 count += min(c[x], c[k - x])
#             seen.add(x)
#             seen.add(k - x)
#     return count


# nums = [1, 2, 3, 4]
# k = 5
# # print(maxOperations(nums, k))  # 2

# nums = [3, 1, 3, 4, 3]
# k = 6
# print(maxOperations(nums, k))  # 1


# SLIDING WINDOW


# LEETCODE 643
# def findMaxAverage(nums, k):
#     # # Sliding Window
#     # # O(n) for time, O(1) for space
#     # left = 0
#     # right = k - 1
#     # total = 0
#     # for i in range(k):
#     #     total += nums[i]
#     # cur_total = total
#     # while right < len(nums) - 1:
#     #     cur_total -= nums[left]
#     #     cur_total += nums[right + 1]
#     #     total = max(cur_total, total)
#     #     left += 1
#     #     right += 1

#     # return total / k

#     # # Sliding Window
#     # # O(n) for time, O(1) for space
#     if len(nums) == 1:
#         return nums[0]

#     window = sum(nums[:k])
#     max_sum = window

#     for i in range(k, len(nums)):
#         window += nums[i]
#         window -= nums[i - k]
#         max_sum = max(max_sum, window)

#     return max_sum / k


# nums = [1, 12, -5, -6, 50, 3]
# k = 4
# print(findMaxAverage(nums, k))  # 12.75000

# nums = [5]
# k = 1
# print(findMaxAverage(nums, k))  # 5.00000

# nums = [0, 4, 0, 3, 2]
# k = 1
# print(findMaxAverage(nums, k))  # 4.00000

# LEETCODE 1456
# def maxVowels(s, k):
#     # Sliding window
#     # O(n) for time, O(n) for space
#     vowels = {"a", "e", "i", "o", "u"}  # use hash table for linear lookup
#     window = s[:k]
#     cur_max = 0
#     for c in window:
#         if c in vowels:
#             cur_max += 1
#     ans = cur_max
#     for i in range(k, len(s)):
#         if s[i] in vowels:
#             cur_max += 1
#         if s[i - k] in vowels:
#             cur_max -= 1
#         ans = max(ans, cur_max)
#     return ans


# s = "abciiidef"
# k = 3
# print(maxVowels(s, k))  # 3

# s = "aeiou"
# k = 2
# print(maxVowels(s, k))  # 2

# s = "leetcode"
# k = 3
# print(maxVowels(s, k))  # 2


# LEETCODE 1004
# def longestOnes(nums, k):
#     # # O(n) for time, O(1) for space
#     # # Sliding window
#     # n = len(nums)
#     # if k >= n:
#     #     return n
#     # left = 0
#     # right = 0
#     # cur_max = 0
#     # while right < len(nums):
#     #     if nums[right] == 0:
#     #         k -= 1
#     #     if k < 0:
#     #         if nums[left] == 0:
#     #             k += 1
#     #         left += 1
#     #     else:
#     #         cur_max = max(cur_max, right - left + 1)
#     #     right += 1

#     # return cur_max

#     # O(n) for time, O(1) for space
#     # Sliding window
#     left = 0
#     cur_max = 0
#     for right, num in enumerate(nums):
#         k -= 1 - num
#         if k < 0:
#             k += 1 - nums[left]
#             left += 1
#         cur_max = max(cur_max, right - left + 1)

#     return cur_max


# nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
# k = 2
# print(longestOnes(nums, k))  # 6

# nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
# k = 3
# print(longestOnes(nums, k))  # 10


# # LEETCODE 1493
# def longestSubarray(nums):
#     # O(n) for time, O(1) for space
#     left = 0
#     cur_max = 0
#     zero_count = 0
#     for right, num in enumerate(nums):
#         if num == 0:
#             zero_count += 1
#         while zero_count > 1:
#             if nums[left] == 0:
#                 zero_count -= 1
#             left += 1
#         cur_max = max(cur_max, right - left)

#     return cur_max


# nums = [1, 1, 0, 1]
# print(longestSubarray(nums))  # 3

# nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
# print(longestSubarray(nums))  # 5

# nums = [1, 1, 1]
# print(longestSubarray(nums))  # 2


# PREFIX SUM

# # LEETCODE 1732
# def largestAltitude(gain):
#     # Prefix sum
#     # O(n) for time, O(1) for space
#     cur_alt = 0  # prefix sum
#     ans = 0
#     for point in gain:
#         cur_alt += point
#         ans = max(ans, cur_alt)
#     return ans


# gain = [-5, 1, 5, 0, -7]
# print(largestAltitude(gain))  # 1

# gain = [-4, -3, -2, -1, 4, 3, 2]
# print(largestAltitude(gain))  # 0


# # LEETCODE 724
# def pivotIndex(nums):
#     # # O(n^2) for time, O(n) for space
#     # # Prefix Sum
#     # sum_left = 0
#     # sum_right = 0
#     # for i in range(len(nums)):
#     #     sum_left += sum(nums[:i])
#     #     sum_right += sum(nums[i + 1 :])
#     #     if sum_left == sum_right:
#     #         return i
#     #     # reset sum_left and sum_right
#     #     sum_left = 0
#     #     sum_right = 0
#     # return -1

#     # O(n) for time, O(1) for space
#     # Prefix Sum
#     sum_left = 0
#     S = sum(nums)
#     sum_right = S
#     for i, num in enumerate(nums):
#         sum_right -= num
#         if sum_left == sum_right:
#             return i
#         sum_left += num
#     return -1


# nums = [1, 7, 3, 6, 5, 6]
# print(pivotIndex(nums))  # 3


# nums = [1, 2, 3]
# print(pivotIndex(nums))  # -1


# nums = [2, 1, -1]
# print(pivotIndex(nums))  # 0


# HASH MAP/ SET
# LEETCODE 2215
# def findDifference(nums1, nums2):
#     # O(n+m) for time, O(max(n,m)) for space
#     # Hashmap
#     dic1 = {}
#     dic2 = {}
#     for i, num in enumerate(nums1):
#         if num not in dic1:
#             dic1[num] = i
#     for i, num in enumerate(nums2):
#         if num not in dic2:
#             dic2[num] = i
#     ans = []
#     ans1 = []
#     ans2 = []
#     for num in dic1:
#         if num not in dic2:
#             ans1.append(num)
#     for num in dic2:
#         if num not in dic1:
#             ans2.append(num)
#     ans.append(ans1)
#     ans.append(ans2)
#     return ans

#     # # O(n) for time, O(n) for space
#     # # Set
#     # set1 = set(nums1)
#     # set2 = set(nums2)
#     # return [list(set1 - set2), list(set2 - set1)]


# nums1 = [1, 2, 3]
# nums2 = [2, 4, 6]
# print(findDifference(nums1, nums2))  # [[1,3],[4,6]]

# nums1 = [1, 2, 3, 3]
# nums2 = [1, 1, 2, 2]
# print(findDifference(nums1, nums2))  # [[3],[]]


# LEETCODE 1207
# def uniqueOccurences(arr):
#     # # O(n) for time, O(n) for space
#     # # Hash Map & Set
#     # dic = {}
#     # for num in arr:
#     #     if num in dic:
#     #         dic[num] += 1
#     #     else:
#     #         dic[num] = 1

#     # occurences = []
#     # for key in dic:
#     #     occurences.append(dic[key])

#     # unique_occurences = set(occurences)
#     # return len(occurences) == len(unique_occurences)

#     # O(n) for time, O(n) for space
#     # Hash Map & Set
#     dic = {}
#     for num in arr:
#         if num in dic:
#             dic[num] += 1
#         else:
#             dic[num] = 1

#     occurences = dic.values()
#     unique_occurences = set(occurences)

#     return len(occurences) == len(unique_occurences)


# arr = [1, 2, 2, 1, 1, 3]
# print(uniqueOccurences(arr))  # true

# arr = [1, 2]
# print(uniqueOccurences(arr))  # false

# arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
# print(uniqueOccurences(arr))  # true

from collections import Counter


# LEETCODE 1657
def closeStrings(word1, word2):
    # Hash Map
    # O(n) for time, O(1) for space
    dic1 = {}
    dic2 = {}
    freq1 = len(word1)
    freq2 = len(word2)
    if freq1 != freq2:
        return False
    for letter in word1:
        if letter not in dic1:
            dic1[letter] = 1
        else:
            dic1[letter] += 1
    for letter in word2:
        if letter not in dic2:
            dic2[letter] = 1
        else:
            dic2[letter] += 1
    for key in dic1:
        if key not in dic2:
            return False

    # Method 1 (sorting)
    # Sort and compare frequency list
    dic1_values_sorted = sorted(dic1.values())
    dic2_values_sorted = sorted(dic2.values())
    return dic1_values_sorted == dic2_values_sorted

    # Method 2


word1 = "abc"
word2 = "bca"
print(closeStrings(word1, word2))  # true

word1 = "a"
word2 = "aa"
print(closeStrings(word1, word2))  # false


word1 = "cabbba"
word2 = "abbccc"
print(closeStrings(word1, word2))  # true


word1 = "abbzzca"
word2 = "babzzcz"
print(closeStrings(word1, word2))  # false
