def twoSum(numbers, target):
    n = len(numbers)
    left = 0
    right = n - 1
    curSum = 0
    while left < right:
        curSum = numbers[left] + numbers[right]
        if curSum == target:
            break
        elif curSum > target:
            right -= 1
        else:
            left += 1
    return [left + 1, right + 1]


numbers = [2, 7, 11, 15]
target = 9
print(twoSum(numbers, target))  # [1,2]

numbers = [2, 3, 4]
taget = 6
print(twoSum(numbers, target))  # [1,3]

numbers = [-1, 0]
target = -1
print(twoSum(numbers, target))  # [1,2]
