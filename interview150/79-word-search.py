def exist(board, word):
    # Time: O(n * m * dfs) -> O(n * m * 4^len(word)) -> O(n * m * 4^n)
    # Space: O(len(word)) -> O(n)
    rows = len(board)
    cols = len(board[0])
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    path = set()

    def dfs(r, c, idx):
        if idx == len(word):
            return True
        if (
            r < 0
            or r >= rows
            or c < 0
            or c >= cols
            or word[idx] != board[r][c]
            or (r, c) in path
        ):
            return False
        # now we find a character that we look for
        path.add((r, c))
        for i in range(4):
            if dfs(r + dr[i], c + dc[i], idx + 1):
                return True
        path.remove((r, c))
        return False

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0] and dfs(r, c, 0):
                return True
    return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(exist(board, word))  # true

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"
print(exist(board, word))  # true

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"
print(exist(board, word))  # false
