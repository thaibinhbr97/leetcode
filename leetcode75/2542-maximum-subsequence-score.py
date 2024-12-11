import heapq


def maxScore(nums1, nums2, k):
    # create a pair of num2 and num1 and sort a pair based on nums2 in a descending order
    pairs = sorted(zip(nums2, nums1), reverse=True)

    # initialize curSum and maxScoring and minHeap
    # curSum used to keep track a sum of k numbers from nums1
    # maxScoring used to track the max scoring result by multiplication of curSum and minimum of kth numbers from nums2
    # since we have the minimum number from nums2 when sorting nums2 in pairs, we only need to consider removing the
    # minimum number from nums1 in curSum using minHeap
    minHeap = []
    curSum = 0
    maxScoring = 0
    for num2, num1 in pairs:
        # add num1 to the heap and keep track of curSum
        heapq.heappush(minHeap, num1)
        curSum += num1

        # if heap size exceeds k, remove the smallest number from the heap and update curSum to have the correct sum
        if len(minHeap) > k:
            popNum = heapq.heappop(minHeap)
            curSum -= popNum

        # if heap size is k, it means that we now have the curSum of k numbers, so we can multiply curSum by num2 which is
        # the lowest number in nums2 at the moment and take the maximum result with the previous maxScoring
        if len(minHeap) == k:
            maxScoring = max(maxScoring, curSum * num2)

    return maxScoring


nums1 = [1, 3, 3, 2]
nums2 = [2, 1, 3, 4]
k = 3
print(maxScore(nums1, nums2, k))  # 12

nums1 = [4, 2, 3, 1, 1]
nums2 = [7, 5, 10, 9, 6]
k = 1
print(maxScore(nums1, nums2, k))  # 30
