class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        return ' '.join(words[::-1])


s = "the sky is blue"

obj = Solution()
print(obj.reverseWords(s))

# Way 2


class Solution:
    def reverseWords(self, s: str) -> str:
        s = (s.strip()).split()
        s.reverse()
        return " ".join(s)
