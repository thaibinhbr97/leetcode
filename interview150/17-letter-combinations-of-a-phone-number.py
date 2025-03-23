def letterCombinations(digits):
    if not digits:
        return []
    mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def backtracking(i, combination):
        if i == len(digits):
            ans.append(combination[:])
            return
        for letter in mapping[digits[i]]:
            backtracking(i + 1, combination + letter)

    ans = []
    backtracking(0, "")
    return ans


digits = "23"
print(letterCombinations(digits))  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]

digits = ""
print(letterCombinations(digits))  # []

digits = "2"
print(letterCombinations(digits))  # ["a","b","c"]
