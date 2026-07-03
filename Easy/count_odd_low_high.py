# for finding odd numbers between 1 to n we have formula (n+1)/2
#  for finding the even number we do (high)//2 - (low-1)//2

# Odd numbers 


low = int(input("Enter low number: "))
high = int(input("Enter high number: "))
count = ((high+1)//2 - (low)//2)
list1= []
for i in range (low, high+1):
  if i%2 !=0:
    list1.append(i)

print(count, list1)



# Even Numbers 

low = int(input("Enter low number: "))
high = int(input("Enter high number: "))
count = ((high)//2 - (low-1)//2)
list1= []
for i in range (low, high+1):
  if i%2 ==0:
    list1.append(i)

print(count, list1)