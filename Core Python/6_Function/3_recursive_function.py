''''
-> A function that call itself is called recursive function.
'''
def factorial(n):
  if n == 1:
    return 1
  else:
    return n * factorial(n - 1)

fact_ans = factorial(5)
print(fact_ans)