candies =[2,3,5,1,3] 
extraCandies = 3


ans = []
for i in candies:
  greatest=i+extraCandies
  for j in candies:
    if greatest>=j:
      ans.append('true')
    else:
      ans.append('false')

print(ans)