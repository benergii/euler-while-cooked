def is_a_factor(number, list_of_factors):

  for n in list_of_factors:
    if number % n == 0:
      return True
    
sum = 0

for n in range(1000):
  if is_a_factor(n, [3, 5]):
    sum += n

print(sum)