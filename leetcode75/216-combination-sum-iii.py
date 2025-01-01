def combinationSum3(k, n):
    """
    find all valid combination of k numbers that sum up to n such that:
    1. only 1 to 9 are used.
    2. each number used at most once

    input:
    k: # of numbers in a combination
    n: a sum to match with a requirement which can be used to find a range of combinations

    output:
    a list of all possible valid combinations
    requirements
    1. must not the same combination twice
    2. the combinations can be returned in any order as long as providing all possible valid combinations in the result

    idea:
    - can use a hashmap to keep track of the existence of each number from 1 to 9 -> make sure 1 to 9 numbers are used at least once

    """
    result = []

    def tryCombination(combination, k, n, start):
        if k == len(combination) and n == 0:
            result.append(combination.copy())
            return
        for i in range(start, 9 + 1):
            combination.append(i)
            tryCombination(combination, k, n - i, i + 1)
            combination.pop()

    tryCombination([], k, n, 1)
    return result


# Test cases
k = 3
n = 15
print(
    combinationSum3(k, n)
)  # [[1,5,9],[1,6,8],[2,4,9],[2,5,8],[2,6,7],[3,4,8],[3,5,7],[4,5,6]]

k = 3
n = 7
print(combinationSum3(k, n))  # [[1,2,4]]

k = 3
n = 9
print(combinationSum3(k, n))  # [[1,2,6],[1,3,5],[2,3,4]]

k = 4
n = 1
print(combinationSum3(k, n))  # []
