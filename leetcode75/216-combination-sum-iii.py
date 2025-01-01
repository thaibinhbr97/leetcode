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
    use backtrack to explore all possible combinations of numbers from 1 to 9
    start with an empty combination and iteratively add numbers to it
    ensure that the sum of the combination does not exceed the target sum 'n'
    and combination contains exactly 'k' numbers
    if a valid combination is found, add it to the result list

    """
    result = []

    # def backtrack(combination, start, sumSoFar):
    #     # base case
    #     if len(combination) == k:
    #         if sumSoFar == n:
    #             result.append(combination)
    #         return

    #     # recursive case
    #     for i in range(start, 9 + 1):
    #         if sumSoFar + i > n:
    #             break
    #         backtrack(combination + [i], i + 1, sumSoFar + i)

    def backtrack(combination, start, sumSoFar):
        # base case
        # if combination size equals k
        if len(combination) == k:
            if sumSoFar == n:
                result.append(combination[:])
            return
        # recursive case
        for i in range(start, 9 + 1):
            # if sumSoFar plus next added number exceeds n, skip further exploration
            if sumSoFar + i > n:
                break

            combination.append(i)  # choose a next number
            backtrack(combination, i + 1, sumSoFar + i)  # explore further
            combination.pop()  # undo the choice (backtrack)

    backtrack([], 1, 0)
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
