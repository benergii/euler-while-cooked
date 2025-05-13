from math import sqrt

# Problem to solve is a + b + sqrt(a^2 + b^2) = 1000

target_value = 1000

def check_problem_solution(a, b):

  if a + b + sqrt(a**2 + b**2) == target_value:
    return True
  else:
    return False

def find_a_and_b():


  for x in range(1, target_value):
    for y in range(2, target_value):

      if check_problem_solution(x, y):
        return x, y
      
def find_product(a, b):

  c = sqrt(a**2 + b**2)

  return int(a * b * c)

print(find_product(*find_a_and_b()))