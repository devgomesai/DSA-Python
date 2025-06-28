from functools import lru_cache

@lru_cache
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(13))

# Create a dict and cal fibonacci

def fibonacci(n, store={}):
    if n in store:  
        return store[n]
    
    if n <= 1:
        return n
    
    store[n] = fibonacci(n-1, store) + fibonacci(n-2, store)
    return store[n]

print(fibonacci(13))