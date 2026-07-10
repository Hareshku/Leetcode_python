# # Formula to find x power n is x power n/2 *2 for even number and for odd numbers x power n/2 *2*x

# class Solution:
#     def findPow(self, x, n):
#         if n == 0:
#             return 1
#         a= self.findPow( x, n//2)
#         if n%2 ==0:
#             return a*a
#         else:
#             return a*a*x
        
#     def myPow(self, x: float, n: int) -> float:
#         if n>=0:
#             return self.findPow(x, n)
#           # for negative values 
#         else:
#             return 1/self.findPow(x, n*(-1))



list1 = [2, 4, 5, 6, 6, 6,4, 3, 4, 2,1, 3, 2, 3, 1, 1, 6, 7, 8, 8, 6, 5, 7, 6,7,7,8 ]
list2 =[]
for i in list1:
    list2.append(list1.count(i))
    # print(i)
print(list1)
print(list2)