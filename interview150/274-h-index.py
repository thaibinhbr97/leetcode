def hIndex(citations):
    # Brute force
    # Time: O(n^2)
    # Space: O(n)
    # n = len(citations)
    # result = 0
    # for h in range(1, n + 1):
    #     num_papers = 0
    #     for i in range(n):
    #         if citations[i] >= h:
    #             num_papers += 1
    #         if num_papers >= h:
    #             result = h
    #             break
    # return result

    # Sorting
    # Time: O(nlogn)
    # Space: O(1)
    # citations.sort(reverse=True)  # sort by descending order
    # result = 0
    # for i, citation in enumerate(citations):
    #     if citation >= i + 1:
    #         result = i + 1
    #     else:
    #         break
    # return result

    # Time: O(n)
    # Space: O(n)
    # Counting sort
    n = len(citations)
    count = [0] * (n + 1)
    for citation in citations:
        count[min(citation, n)] += 1  # if citations > n, consider it for count[n]
    papers = 0
    for h in range(n, -1, -1):
        papers += count[h]
        if papers >= h:
            break
    return h


citations = [100]
print(hIndex(citations))  # 1

citations = [5, 1, 2, 8, 9, 3]
print(hIndex(citations))  # 3

citations = [6, 6, 6, 6, 6, 6]
print(hIndex(citations))  # 6

citations = [3, 0, 6, 1, 5]
print(hIndex(citations))  # 3

citations = [1, 3, 1]
print(hIndex(citations))  # 1
