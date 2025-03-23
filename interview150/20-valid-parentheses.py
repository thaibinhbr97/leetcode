class Solution:
    def isValid(self, s: str) -> bool:
        # Time: O(n) for time since each character is processed once through the string s
        # Space: O(n) for space since all opening brackets are stored in the stack through string s

        # use stack to keep track of opening parentheses
        stack = []
        # use dictionary to keep track of valid closing parentheses
        bracket_map = {")": "(", "]": "[", "}": "{"}
        for char in s:
            # if character is an opening bracket, keep appending to the stack
            if char not in bracket_map:
                stack.append(char)
            # character is now a closing bracket
            else:
                # if stack is empty or the top of the stack does not match the corresponding opening bracket , return False
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                # if the top of the stack matches the corresponding opening bracket, pop it
                stack.pop()
        # stack should be empty if all opening brackets are removed to be valid
        return not stack
