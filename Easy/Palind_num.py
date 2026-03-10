input_value = input("Enter a number: ")
def is_palindrome(input_value):
    if input_value == input_value[::-1]:
        return True
    else:
        return False
      
result = is_palindrome(input_value)
print(f"Is the number a palindrome? {result}")


# optimal solution:
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0 or (x and x % 10 == 0):
#             return False
#         y = 0
#         while y < x:
#             y = y * 10 + x % 10
#             x //= 10
#         return x in (y, y // 10)