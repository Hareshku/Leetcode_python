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


# time complexity O(3**n)
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
# time complexity O(log n)
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n<=0: return False
#         if n==1: return True
#         if n%2!=0: return False

#         return self.isPowerOfTwo(n//2)


# Find if a given number power of 3
# time complexity O(log n)
# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         if n <=0:
#             return False
#         if n ==1:
#             return True
#         if n%3!=0:
#             return False
#         return self.isPowerOfThree(n//3)

# Find the GCD of two numbers
# Euclidean formula is used to calculate GCD 
# time complexity O(log(min(a,b))) 
# def gcd(a,b):
#     if b==0:
#         return a 
#     return gcd(b, a%b)

# def lcm(a, b):      #Find LCM
#     return a*b//gcd(a,b) 

# print(gcd(15, 50))
# print(lcm(15, 50))


# Find x to the power n 
# time complexity O(log n) 
class Solution:
    def findPow(self, x, n):
        # base case 
        if n == 0:
            return 1
        # recursive case 
        a = self.findPow(x, n//2)
        # If power is even 
        if n % 2== 0:
            return a*a
        else:  #If power is odd
            return a*a*x
        

    def myPow(self, x: float, n: int) -> float:
        if n>=0: #If power is positive
            return self.findPow(x, n)
        else:  # If power is nagative (-)
            return 1/ self.findPow(x, n*(-1))
        