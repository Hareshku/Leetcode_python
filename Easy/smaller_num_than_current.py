list1 = [8, 1, 2, 2, 3]
list2 =[]
for i in list1:
  COUNT = 0
  for j in list1:
    if j<i:
      COUNT+=1 
  list2.append(COUNT)
  
print(list2)
  