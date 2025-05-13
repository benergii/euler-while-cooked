def sum_of_squares(upper_bound):

  s = 0

  for n in range(upper_bound + 1):
    s += n ** 2
  
  return s

def square_of_sums(upper_bound):

  s = 0
  
  for n in range(upper_bound + 1):
    s += n
  
  return s ** 2

upper = 100

print(square_of_sums(upper) - sum_of_squares(upper))