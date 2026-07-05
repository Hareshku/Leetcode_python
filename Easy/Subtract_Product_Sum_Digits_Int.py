n=234
temp = n
sum =0
product= 1
while temp>0:
  r= temp%10
  sum+=r
  product*=r
  temp//=10

result= product-sum

print(result)
