def is_a_divisor(n, list_of_divisors):

  for d in list_of_divisors:

    if n % d != 0:
      return False
  
  return True

list_of_primes = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

starting_num = list_of_primes[-1]

breakout_var = False

while breakout_var == False:
  
  starting_num = starting_num + list_of_primes[-1]

  breakout_var = is_a_divisor(starting_num, list_of_primes)

print(f'Final number is {starting_num}')