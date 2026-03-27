class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).index(s, 1) < len(s)

s="abab"

obj=Solution()
print(obj.repeatedSubstringPattern(s))