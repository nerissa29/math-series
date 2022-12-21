def fibonacci(n):

    # checks if n <= 0, then return 0
    if n == 0:
        return 0
    # checks if n == 1, then return 1
    elif n == 1 or n == 2:
        return 1
    # checks if n < 0
    elif n < 0:
        return "Please enter numbers >= 0"
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def lucas(n):
    #chceks if n <= 0, then return 2
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n < 0:
        return "Please enter numbers >= 0"
    else:
        return lucas(n - 1) + lucas(n - 2)
