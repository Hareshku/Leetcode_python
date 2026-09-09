# # Lecture-1

# # FizzBuzz
# Time complexity O(n)
# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
#         ans = []

#         for i in range(1, n+1):
#             if i%3 == 0 and i%5==0:
#                 ans.append("FizzBuzz")
#             elif i%3==0:
#                 ans.append("Fizz")
#             elif i%5 == 0:
#                 ans.append("Buzz")
#             else:
#                 ans.append(str(i))
#         return ans


# # Count Odd numbers in an interval range
# Time complexiy O(1)
# class Solution:
#     def countOdds(self, low: int, high: int) -> int:
#         # formula to find odd numbers from 1 to n : (n+1)/2. From 1-low= low-1

#         return (high+1)//2- (low//2)

# # Other way
#  Time complexity O(n)
# ans = 0
# for i in range(low, high+1):
#     if i%2 !=0:
#         ans+=1
# print(ans)


# # Kids with greatest numbers of Candies
# Big O(n)
# class Solution:
#     def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
#         new_list =[]
#         maxCandies = max(candies)
#         for i in candies:
#             if (i+extraCandies)>=maxCandies:
#                 new_list.append(True)
#             else:
#                 new_list.append(False)

#         return new_list



# # Palindrome number
# O(log n)
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         temp = x
#         reverse= 0
#         while temp >0:
#             r = temp%10
#             reverse=(reverse*10+r)
#             temp//=10
#         # if x == reverse:
#         #     return True
#         # else:
#         #     return False
#         return reverse==x
        
# # Substract the product and sum of digits of an integer
#  O(log n)
# class Solution:
#     def subtractProductAndSum(self, n: int) -> int:
#         sum =0
#         product =1
#         while n>0:
#             r = n%10
#             n //=10
#             sum +=r
#             product*=r
#         return product - sum
        

# # Count the digits that divides a number
# O(log n)
# class Solution:
#     def countDigits(self, num: int) -> int:
#         ans = 0
#         temp =num

#         while temp>0:
#             r = temp%10
#             if num %r == 0:
#                 ans+=1
#             temp//=10
#         return ans


# # How many numbers are the small than the current number 
# O(n**2)
# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         ans =[]
#         for i in nums:
#             count = 0
#             for j in nums:
#                 if i>j:
#                     count+=1
#             ans.append(count)
#         return ans
        

# Sort an array 
# first way using buildtin method
O(n log n)
numbers = [5, 3, 8, 1, 2]
numbers.sort() # Sorts in ascending order
print(numbers) 

# 2nd way without builtin method 
O(n**2)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(n-i-1):
                if nums[j]>nums[j+1]:
                    temp = nums[j]
                    nums[j]= nums[j+1]
                    nums[j+1]=temp
        return nums