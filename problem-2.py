def next_fib_num(n1, n2):

  next_num = n1 + n2

  return n2, next_num

n1 = 0
n2 = 1
sum = 0

while n2 < 4000000:

  n1, n2 = next_fib_num(n1, n2)

  if n2 % 2 == 0:
    sum += n2

print(sum)