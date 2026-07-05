n=234
temp = n
sum_ =0
product= 1
while temp>0:
  r= temp%10
  sum_+=r
  product*=r
  temp//=10

result= product-sum_

print(result)
