# Function to determine prime
def is_it_prime(num):
  
  divisors = []
  for n in range(1, num):
    if num % n == 0: divisors.append(n)

  return False if len(divisors) > 2 else True

primes = []

# ARBITRARY UPPER BOUND - FOR VIBES ONLY
prime_upper_bound = 10000

# build a list of all primes up until the upper bound
for n in range(1, prime_upper_bound):
  if is_it_prime(n): primes.append(n)

# The number we are trying to prime factorise
num = 600851475143

# LETS CHECK ALL THOSE PRIMES AND SEE WHICH ONES ARE FACTORS
for n in primes:
  if num % n == 0:
    print(f'{n} is a factor')