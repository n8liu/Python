''' A basic recursion example: 
Print all numbers n 
'''

# will print 0 too
def print_until_0(n):
    if n < 0:
        return 0
    print(n)
    return print_until(n-1)

# will not print 0, but 1 as the last item
def print_until(n):
    if n == 0:
        return 0
    print(n)
    return print_until(n-1)

def print_until_1(n):
    if n == 0:
        return 0
    else:
        print(n)
        return print_until(n-1)

'''
Add all numbers until n
'''
def add_all(n):
    if n == 0:
        return 0
    else:
        return n + add_all(n-1)

'''
Fibonacci
'''
def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)