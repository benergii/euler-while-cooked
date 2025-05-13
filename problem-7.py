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