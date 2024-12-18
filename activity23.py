def factorial(number):
  """ This Function again is for calculating Factorial Numbers, just provide a value, and it would automatincally compute the factorial"""
  fact = 1
  for x in range(number, 0, -1):
    fact *= 1
    return fact
print(f"The factorial of 13 is {factorial(13)}")
