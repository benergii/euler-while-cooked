# Idea here is to start with a list of prime numbers, starting with just 2
# Then we increment up every odd number FROM 2, and check to see if it evenly divides by any of our primes
# If it does not, then it's a prime number - so add it to the list
# Every time we add a number to the list, we check the lists length
# If the length equals the target prime, then print it and stop the loop

def not_divisible_by_any(n, list_of_factors):

  for l in list_of_factors:
    if n % l == 0:
      return False
  return True
  
set_of_primes = [2]

nth_prime = 10001

upper_bound = 1000000000000

for n in range(3, upper_bound, 2):

  if not_divisible_by_any(n, set_of_primes):
    set_of_primes.append(n)

    if len(set_of_primes) == nth_prime:
      print(f'{nth_prime}th prime is {set_of_primes[-1]}')
      break