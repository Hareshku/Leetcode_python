class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'()', '[]', '{}'}
        for c in s:
            if c in '({[':
                stack.append(c)
            elif not stack or stack.pop() + c not in d:
                return False
        return not stack
  
  # I want for the following five examples to test the function:

sol = Solution()

print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
print(sol.isValid("([])"))
print(sol.isValid("([)]"))
print(sol.isValid("()"))
