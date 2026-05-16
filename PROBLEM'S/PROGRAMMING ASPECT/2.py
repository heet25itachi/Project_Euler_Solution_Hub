limit = 4000000
total_sum = 0
a, b = 1, 2  # starting values specified in the problem 

while a <= limit:
  if a % 2 == 0:
    total_sum += a
  a, b = b, a + b

print(total_sum)   #Output: 4613732
