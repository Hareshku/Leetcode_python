num = int(input("Enter the number: "))

# temp =num
# reverse=0
# while temp>0:
#   r= temp%10
#   reverse = reverse*10+r
#   temp//=10
  
# result = "Yes palindrome" if reverse==num else "not a palindrome"
  
# print(result)
reverse= int(str(num)[:: -1])

if reverse== num:
  print("palindrome")
else:
  print("not")