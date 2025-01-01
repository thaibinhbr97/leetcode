def letterCombination(digits):
    res = []
    if not digits:
        return res

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

    def backtrack(idx, combination):
        if idx == len(digits):
            res.append(combination[:])
            return
        for letter in mapping[digits[idx]]:
            backtrack(idx + 1, combination + letter)

    backtrack(0, "")
    return res


digits = "23"
print(letterCombination(digits))  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]

digits = ""
print(letterCombination(digits))  # []

digits = "2"
print(letterCombination(digits))  # ["a","b","c"]
