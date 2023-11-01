"""
Challenge 1.1
Factorial of a number using recursion
"""
def fact(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact(n-1)

n= int(input("Enater a number: "))
print('Factorial of {} is {}'.format(n,fact(n)))