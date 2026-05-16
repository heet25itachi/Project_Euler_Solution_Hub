limit = 4000000
total_sum = 0
e1, e2 = 2, 8  # First two even terms 

while e1 <= limit:
    total_sum += e1
    e1, e2 = e2, 4 * e2 + e1

print(total_sum)   #Output: 4613732
