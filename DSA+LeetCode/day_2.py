# Recursion: A process in which a function calls itself directly or indirectly is call recursion and function is call recursive fuction

# Print numbers from 1 to n using Recursion 

# using while loop 

# i =1
# n= 5

# while i<=5:
#     print(i, end =" ")
#     i+=1


# Using Recursion 

# def print_Numbers(i, n):

#     # base case/ stoping condition
#     if i>n:
#         return
    
#     # Recursive case 
#     print(i, end =" ")
#     print_Numbers(i+1, n)

# print_Numbers(1, 5)


# Factorial 

# using loop
# time complexity O(n)
# i = 1
# n = 5
# fact = 1

# while i<=5:
#     fact *=i
#     i+=1

# print(fact)

# using Recursion
# time complexity O(n)
# def factorial(n):
#     # base case 
#     if n ==0:
#         return 1
    
#     return n*factorial(n-1)
# print(factorial(4))

# Recursive stack 
# time complexity O(n)
# def factorial(n):
#     # base case 
#     if n ==0:
#         return 
    
#     factorial(n-1)
#     print(n, end=" ")
# factorial(4) # 1, 2, 3, 4


# Recursive Tree 
# time complexity O(2**n) exponential

# def fib(n):
#    if n==0 or n == 1:
#     return n

#    return fib(n-1)+fib(n-2)

# print(fib(6))

# def fib(n):
#    if n==0:
#     return 0

#    if n == 1 or n ==2:
#     return 1

#    return fib(n-1)+fib(n-2)+fib(n-3)

# print(fib(25))

# class Solution:
#     def tribonacci(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1 or n==2:
#             return 1
        
#         return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)

# Find if a givn number is the power of 2 

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0: return False
        if n==1: return True
        if n%2!=0: return False

        return self.isPowerOfTwo(n//2)

    