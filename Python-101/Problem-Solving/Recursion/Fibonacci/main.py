def fibonacci(n):
	if n is 0 or n is 1:
		return n
	return fibonacci(n - 1) + fibonacci(n - 2)
	
	
'''
Better Solution, using memory for storing existing Fibonacci number (Recursion with memoization)
'''

memory = {}
def fibonacci(n):
    if n < 2:
        return n
    if not n in memory.keys():
        memory[n] = fibonacci(n-1) + fibonacci(n-2)
    return memory[n]
