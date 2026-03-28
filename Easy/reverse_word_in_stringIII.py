class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([t[::-1] for t in s.split(' ')])
      
      
s = "Let's take LeetCode contest"
obj= Solution()
print(obj.reverseWords(s))