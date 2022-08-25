class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['{', '[', '(']
        stack = []
        for bracket in s:
            if bracket in opening:
                stack.append(bracket)
            elif stack:
                if bracket == ')' and stack[-1] != '(':
                    return False
                if bracket == ']' and stack[-1] != '[':
                    return False
                if bracket == '}' and stack[-1] != '{':
                    return False
                stack.pop()
            else:
                return False
        return len(stack) == 0
