def is_palindrome(number):
  string_number = str(number)

  reversed_string_number = string_number[::-1]

  return True if string_number == reversed_string_number else False

palindrome_product = 0

for x in range(999, 100, -1):
  for y in range(999, 100, -1):

    if is_palindrome(x * y) and x * y > palindrome_product:
      palindrome_product = x * y

print(palindrome_product)