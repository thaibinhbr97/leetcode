def generateParenthesis(n):
    def backtracking(path, openCount, closeCount):
        if openCount == n and closeCount == n:
            ans.append(path)
        # if there are open slots, add an opening paren
        if openCount < n:
            backtracking(path + "(", openCount + 1, closeCount)
        # if there is not enough closing parens to balance out open parens, add a closing paren
        if closeCount < openCount:
            backtracking(path + ")", openCount, closeCount + 1)

    ans = []
    backtracking("", 0, 0)
    return ans


n = 3
print(generateParenthesis(n))  # ["((()))","(()())","(())()","()(())","()()()"]

n = 1
print(generateParenthesis(n))  # ["()"]
